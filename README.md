# Temperature Conversion Tool

This Python program allows users to convert temperatures between different temperature scales, including **Celsius**, **Fahrenheit**, and **Kelvin**. It supports six different conversion options and provides accurate results using the appropriate formulas.

---

## **Table of Contents**
1. [Features](#features)
2. [Supported Conversions](#supported-conversions)
3. [How to Run](#how-to-run)
4. [Program Workflow](#program-workflow)
5. [Example Interaction](#example-interaction)
6. [Dependencies](#dependencies)
7. [License](#license)

---

## **Features**
- **Supported Temperature Scales**: Celsius, Fahrenheit, and Kelvin.
- **Six Conversion Options**:
  - Celsius ↔ Fahrenheit
  - Celsius ↔ Kelvin
  - Fahrenheit ↔ Kelvin
- **Interactive Interface**:
  - Displays a menu of conversion options for easy navigation.
  - Allows users to convert multiple temperatures in a single session.
  - Provides detailed output of the original and converted temperatures.
- **User-Friendly Prompts**:
  - Handles invalid choices and prompts for valid input.
  - Continues running until the user explicitly decides to quit.

---

## **Supported Conversions**
The program supports the following conversions:
1. **Celsius to Fahrenheit**:
   \[
   F = \left( \frac{9}{5} \times C \right) + 32
   \]
2. **Celsius to Kelvin**:
   \[
   K = C + 273.15
   \]
3. **Fahrenheit to Celsius**:
   \[
   C = \frac{5}{9} \times (F - 32)
   \]
4. **Fahrenheit to Kelvin**:
   \[
   K = \frac{5}{9} \times (F - 32) + 273.15
   \]
5. **Kelvin to Celsius**:
   \[
   C = K - 273.15
   \]
6. **Kelvin to Fahrenheit**:
   \[
   F = \left( \frac{9}{5} \times (K - 273.15) \right) + 32
   \]

---

## **How to Run**
1. Save the program as `temperature_conversion.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the program.
4. Run the program:
   ```bash
   python3 temperature_conversion.py
