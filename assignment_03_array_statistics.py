# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def find_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def find_average(numbers):
    if not numbers:
        return 0
    return find_sum(numbers) / len(numbers)

def find_maximum(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for n in numbers[1:]:
        if n > maximum:
            maximum = n
    return maximum

def find_minimum(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for n in numbers[1:]:
        if n < minimum:
            minimum = n
    return minimum

def main():
    try:
        count = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a positive integer.")
        return

    if count <= 0:
        print("Error: Please enter a positive integer.")
        return

    numbers = []
    for i in range(count):
        # allow integer or float input
        try:
            num = float(input(f"Enter number {i + 1}: "))
        except ValueError:
            print("Error: Invalid number entered.")
            return
        numbers.append(num)

    print("\nResults:")
    print(f"Sum:     {find_sum(numbers)}")
    print(f"Average: {find_average(numbers)}")
    print(f"Maximum: {find_maximum(numbers)}")
    print(f"Minimum: {find_minimum(numbers)}")


if __name__ == "__main__":
    main()
