#### Welcome to my FizzBuzz program. 
#### Just a basic program for beginners like myself to practice with

def fizz_buzz(start, upTo):
    """Generate and display the FizzBuzz sequence from start to upTo."""
    for num in range(start, upTo + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("• FizzBuzz")
        elif num % 3 == 0:
            print("• Fizz")
        elif num % 5 == 0:
            print("• Buzz")
        else:
            print("• ", num)

def get_positive_input(number):
    """Get a positive integer input from the user."""
    while True:
        try:
            value = int(input(number))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    print("Welcome to the FizzBuzz program!")
    start = get_positive_input("Enter the start number: ")
    up_to = get_positive_input("Enter the end number: ")

    fizz_buzz(start, up_to)