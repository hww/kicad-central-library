# Central Library Project

Component Categories

The list of component categories was intentionally chosen as the most universal and predictable format for technical systems. Below is the list of groups:

- audio – Audio components (microphones, speakers, codecs).
- circuit_protection – Circuit protection (fuses, TVS diodes, varistors).
- display – Displays, screens, indicators.
- filter – Filters (EMI filters, ferrite beads).
- mechanical – Enclosures, mounting hardware, heatsinks.
- switch – Buttons, switches, relays.
- transistor – Transistors (BJTs, MOSFETs, IGBTs).
- battery – Batteries, battery connectors.
- connector – Connectors (USB, HDMI, terminals).
- documentation – Documentation symbols (for schematic annotations).
- ic – Integrated circuits (preferably not split further, but subcategories can be added as tags).
- oscillator – Crystals, oscillators.
- testpoint – Test points.
- capacitor – Capacitors (ceramic, electrolytic).
- diode – Diodes (Zener, Schottky, etc.).
- fpga – FPGAs and related components.
- inductor – Inductors, chokes.
- resistor – Resistors, thermistors.
- transformer – Transformers.
- optics – Optoelectronics (optocouplers, photodiodes, IR receivers).
- led – LEDs (can be under optics, but if numerous, keep separate).
- sensor – Sensors (temperature, pressure, Hall effect).
- memory – Memory (EEPROM, Flash, SD cards; can stay under ic, but separate if extensive).
- rf – RF components (antennas, RF modules, for wireless projects).

Naming Conventions

This category list has a fixed structure and should not be expanded further. To ensure maximum compatibility and consistency, all filenames and tables use snake_case notation—lowercase Latin letters with underscores as separators (e.g., circuit_protection.csv, power_supply.csv).

This approach ensures:

- No case-sensitivity issues (critical for Linux/Unix).
- No need for special character escaping.
- Compliance with best practices for machine-readable formats.

This naming standard is especially important for:

- Version control systems (Git).
- CI/CD pipelines.
- Automated data processing scripts.
- Cross-platform projects.
