import numpy as np 
import random as random
from math import floor, ceil
numbersInput = input("Enter numbers: ")
numberList = [] 
for num in numbersInput.split(","):  
    numberList.append(int(float(num)))  
numbersArray = np.array(numberList)
bitwiseOrResult = numberList[0]
for num in numberList[1:]:
    bitwiseOrResult  |= num
bitwiseXOrResult = numberList[0]
for num in numberList[1:]:
    bitwiseXOrResult  ^= num   
print("The list of numbers:", numberList)
print("List:", numberList)
print("Sum:", sum(numberList))
print("Average:", sum(numberList) / len(numberList))
print("Max:", max(numberList))
print("Min:", min(numberList))
print("Bitwise OR result:",bitwiseOrResult )
print("Bitwise XOR result:",bitwiseXOrResult )
print("For 2 Numbers")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operation = input("What operation? (+, -, *, /, %, pow, abs, floor, ceil): ").strip().lower()
if operation == '+':
    print(f"Addition: {x + y}")
elif operation == '-':
    print(f"Subtraction: {x - y}")
elif operation == '*':
    print(f"Multiplication: {x * y}")
elif operation == '/':
    if y == 0:
        print("Error: Division by zero!")
    else:
        print(f"Division: {x / y}")
elif operation == '%':
    if y == 0:
        print("Error: Modulus by zero!")
    else:
        print(f"Modulus: {x % y}")  
elif operation == 'pow':
    print(f"Power: {pow(x, y)}")
elif operation == 'abs':
    print(f"Absolute of {x}: {abs(x)}")
    print(f"Absolute of {y}: {abs(y)}")
elif operation == 'floor':
    print(f"Floor of {x}: {floor(x)}")
    print(f"Floor of {y}: {floor(y)}")
elif operation == 'ceil':
    print(f"Ceil of {x}: {ceil(x)}")
    print(f"Ceil of {y}: {ceil(y)}")
else:
    print("Invalid operation!")
print("Random number")
random = random.random()
percentage = random * 100
print("percentage of ",random ,"= ",percentage )