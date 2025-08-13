import csv
import json
import os
import sys

# Used for constructing initial DB config file from bunch of CSV files


def remove_file_extension(file_name):
    file_name = str.replace(file_name, ".xlsx","")
    file_name = str.replace(file_name, ".xls","")
    return file_name

def process_csv_file(file_path):
    # Получаем имя файла без расширения
    filename = os.path.splitext(os.path.basename(file_path))[0]
    
    # Читаем CSV файл
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)  # не преобразует в словарь
        first_row = next(reader)  # читаем заголовок вручную

        if first_row is None:
            return None
        
        # Получаем текст из ячейки TEXT
        #text_value = first_row.get('TEXT', '')
        filename = remove_file_extension(filename)

        # Создаем структуру данных
        result = {
            "name": filename,
            "table": filename,
            "key": "Part Number",
            "symbols": "Symbol",
            "footprints": "Footprint",
            "fields": [
                #{
                #    "column": text_value,
                #    "name": text_value,
                #    "visible_on_add": False,
                #    "visible_in_chooser": True,
                #    "show_name": False
                #}
            ]
        }
        
        # Добавляем остальные записи из строки (кроме TEXT)
        for value in first_row:
            result["fields"].append({
                "column": value,
                "name": value,
                "visible_on_add": False,
                "visible_in_chooser": True,
                "show_name": False
            })
        
        return result

def find_csv_files(directory):
    """Рекурсивно находит все CSV файлы в директории"""
    csv_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files


def save_csv_file(file_path):
    """
    Сохраняет первую строку CSV файла в новый файл с тем же именем.
    
    Args:
        file_path (str): Путь к исходному CSV файлу
        
    Returns:
        bool: True если операция успешна, False если файл уже существует или произошла ошибка
    """
    # Проверяем существование исходного файла
    if not os.path.exists(file_path):
        print(f"Ошибка: файл {file_path} не существует")
        return False
    
    # Получаем имя нового файла без расширения
    filename = os.path.splitext(os.path.basename(file_path))[0]
    save_name = remove_file_extension(filename) + ".csv"
    
    # Проверяем, не существует ли уже целевой файл
    if os.path.exists(save_name):
        print(f"Ошибка: файл {save_name} уже существует")
        return False
    
    try:
        # Читаем исходный файл
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            try:
                first_row = next(reader)  # Получаем первую строку
            except StopIteration:
                print(f"Ошибка: файл {file_path} пуст")
                return False
            
            # Записываем в новый файл
            with open(save_name, mode='w', encoding='utf-8', newline='') as save_csv_file:
                writer = csv.writer(save_csv_file)
                writer.writerow(first_row)
        
        return True
    
    except Exception as e:
        print(f"Ошибка при обработке файла: {str(e)}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory", file=sys.stderr)
        sys.exit(1)
    
    csv_files = find_csv_files(directory)
    
    if not csv_files:
        print(f"No CSV files found in {directory}", file=sys.stderr)
        sys.exit(1)
    
    libraries = []
    for csv_file in csv_files:
        try:
            processed = process_csv_file(csv_file)
            if processed:
                libraries.append(processed)
        except Exception as e:
            print(f"Error processing {csv_file}: {str(e)}", file=sys.stderr)
    
    config = {
    "meta": {
            "version": 0
        },
        "name": "KiCad Database Library",
        "description": "KiCad components database",
        "source": {
            "type": "odbc",
            "dsn": "",
            "username": "",
            "password": "",
            "timeout_seconds": 10,
            "connection_string": "DRIVER={SQLite3 ODBC Driver};DATABASE=${CWD}/parts.sqlite"
        },
        "libraries":libraries
    }
    for csv_file in csv_files:
        try:
            save_csv_file(csv_file)
        except Exception as e:
            print(f"Error processing {csv_file}: {str(e)}", file=sys.stderr)
            
    with open("databook.kicad_dbl.json", mode='w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(config, indent=2, ensure_ascii=False))
    # print(json.dumps(config, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()