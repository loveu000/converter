def decimal_to_binary(decimal_num):
    """Converts a decimal number to its binary representation."""
    binary_num = bin(decimal_num)[2:]
    return binary_num

def binary_to_decimal(binary_num):
    """Converts a binary number (as a string) to its decimal representation."""
    decimal_num = int(binary_num, 2)
    return decimal_num

def main():
    print("Welcome to the Decimal-Binary Converter!")

    while True:
        print("\nChoose an option:")
        print("1. Convert Decimal to Binary")
        print("2. Convert Binary to Decimal")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            decimal_number = int(input("Enter a decimal number: "))
            binary_number = decimal_to_binary(decimal_number)
            print(f"The binary representation of {decimal_number} is: {binary_number}")
        elif choice == "2":
            binary_string = input("Enter a binary number: ")
            decimal_number = binary_to_decimal(binary_string)
            print(f"The decimal representation of {binary_string} is: {decimal_number}")
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
