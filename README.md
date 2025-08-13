# Central Library Project

This is my personal component library, currently serving as a structured skeleton. While empty at the moment, it follows a carefully designed categorization system for optimal organization and future expansion.

## Component Categories

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

## Library Structure Principles

1. Fixed Taxonomy
 
  - The category list is intentionally finite and closed
  - New components fit existing categories

2. Naming Convention

  - Strict snake_case format (e.g., circuit_protection)
  - Lowercase ASCII only
  - Underscore as word separator

3. Technical Advantages

  - Case-insensitive compatibility (critical for cross-platform use)
  - No special character handling required
  - Machine-readable optimization

## Implementation Notes

This structure is particularly valuable for:

✔ Version control systems (Git)

✔ Automated CI/CD workflows

✔ Script-based component management

✔ Multi-platform development environments

The empty skeleton will be populated while strictly maintaining these organizational principles to ensure long-term usability and consistency.
