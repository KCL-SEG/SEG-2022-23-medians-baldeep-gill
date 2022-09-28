"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

length = len(numbers)
numbers.sort()
if length == 1:
    print(numbers[0])
elif length % 2 == 0:
    average = (numbers[length//2] + numbers[(length//2) - 1]) / 2
    print(average)
else:
    print(numbers[length // 2])
