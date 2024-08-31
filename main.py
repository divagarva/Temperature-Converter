# Temperature Converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def convert_temperature():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")

    choice = input("Choose a conversion (1/2/3): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
        print(f"{celsius}°C is {celsius_to_kelvin(celsius):.2f}K")

    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
        print(f"{fahrenheit}°F is {fahrenheit_to_kelvin(fahrenheit):.2f}K")

    elif choice == '3':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin}K is {kelvin_to_celsius(kelvin):.2f}°C")
        print(f"{kelvin}K is {kelvin_to_fahrenheit(kelvin):.2f}°F")

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    convert_temperature()
