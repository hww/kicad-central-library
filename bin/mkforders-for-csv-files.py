#!/bin/python
import os
import sys
from pathlib import Path

def process_csv_files(source_dir, target_dir):
    """
    Создает директории для каждого CSV файла в целевой папке
    
    Args:
        source_dir (str): Папка с исходными CSV файлами
        target_dir (str): Папка для создания директорий
    """
    # Создаем целевую папку если не существует
    Path(target_dir).mkdir(parents=True, exist_ok=True)
    
    # Ищем CSV файлы
    for item in Path(source_dir).rglob('*.csv'):
        # Получаем имя директории без расширения
        dir_name = item.stem
        target_path = Path(target_dir) / dir_name
        
        # Создаем директорию если не существует
        try:
            target_path.mkdir(exist_ok=True)
            print(f"Создана директория: {target_path}")
        except Exception as e:
            print(f"Ошибка при создании {target_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py <исходная_папка> <целевая_папка>")
        sys.exit(1)
    
    source_directory = sys.argv[1]
    target_directory = sys.argv[2]
    
    if not Path(source_directory).exists():
        print(f"Ошибка: исходная папка {source_directory} не существует")
        sys.exit(1)
    
    process_csv_files(source_directory, target_directory)
    print("Обработка завершена")
