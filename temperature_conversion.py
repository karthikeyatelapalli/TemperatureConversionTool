# Temperature Conversion
'''
Description: A given temperature in one temperature scale can be converted using this program to a different temperature 
scale that is defined. The user is given the opportunity to choose one of six conversions, including Celsius to Fahrenheit,
Celsius to Kelvin, Fahrenheit to Celsius, Fahrenheit to Kelvin, Celsius to Celsius, and Kelvin to Fahrenheit. When a 
user enters a temperature to be converted, the software uses the proper conversion formula to determine the converted
temperature. Along with the user's original temperature and the chosen conversion option, the program also shows 
the converted temperature. The user is then prompted with the option to convert another temperature, and the software
keeps running until they type "No".
'''

def function():
    # prints the user's available conversion options.
    print("Here are your options:")
    print("1. Convert from Celsius to Fahrenheit")
    print("2. Convert from Celsius to Kelvin")
    print("3. Convert from Fahrenheit to Celsius")
    print("4. Convert from Fahrenheit to Kelvin")
    print("5. Convert from Kelvin to Celsius")
    print("6. Convert from Kelvin to Fahrenheit")

def celsius_to_fahrenheit(temperature):
    # The temperature is changed from Celsius to Fahrenheit.
    return (9 / 5) * temperature + 32

def celsius_to_kelvin(temperature):
    # temperature conversion from Celsius to Kelvin.
    return temperature + 273.15

def fahrenheit_to_celsius(temperature):
    # Fahrenheit to Celsius temperature conversion.
    return (5 / 9) * (temperature - 32)

def fahrenheit_to_kelvin(temperature):
    #The temperature is changed from Fahrenheit to Kelvin.
    return (5 / 9) * (temperature - 32) + 273.15

def kelvin_to_celsius(temperature):
    # temperature conversion from Kelvin to Celsius.
    return temperature - 273.15

def kelvin_to_fahrenheit(temperature):
    # The temperature's conversion from Kelvin to Fahrenheit.
    return (9 / 5) * (temperature - 273.15) + 32


def main():
    #The temperature conversion is carried out and displayed.
    ask_again = True
    while ask_again:

        print("This program will convert temperatures for you!")
        
        # The user's conversion choices will be printed.
        function()
        # To select a conversion choice, it asks the user.

        conversion_choice = int(input("Please select an option: "))
        while conversion_choice < 1 or conversion_choice > 6:
            conversion_choice = int(input("Invalid choice. Please re-select an option: "))

        # requesting the user to input a temperature.
        user_input_temperature = float(input("Enter a temperature: "))

        # Convert the temperature in accordance with the user's selected conversion method, then shows the outcome.
        temperature_dictionary = {1: f"{user_input_temperature} degrees Celsius is {celsius_to_fahrenheit(user_input_temperature):.2f} degrees Fahrenheit.",
        2: f"{user_input_temperature} degrees Celsius is {celsius_to_kelvin(user_input_temperature):.2f} Kelvin.",
        3: f"{user_input_temperature} degrees Fahrenheit is {fahrenheit_to_celsius(user_input_temperature):.2f} degrees Celsius.",
        4: f"{user_input_temperature} degrees Fahrenheit is {fahrenheit_to_kelvin(user_input_temperature):.2f} Kelvin.",
        5: f"{user_input_temperature} degrees Kelvin is {kelvin_to_celsius(user_input_temperature):.2f} degrees Celsius.",
        6: f"{user_input_temperature} degrees Kelvin is {kelvin_to_fahrenheit(user_input_temperature):.2f} degrees Fahrenheit."}  

        print(temperature_dictionary[conversion_choice])

        # Inquire about the user's desire to change another temperature.
        print()
        ask_again = False if input("would you like to convert another temperature? ").lower() == "no" else True

if __name__ == "__main__":
    main()          
