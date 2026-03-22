## Find the Location of the set bit in a given number

def findSetBit(n):
    if n == 0:
        return 0

    position = 1
    print(f"Binary representation of {n} is: {bin(n)}")
    while (n & 1) == 0:
        n = n >> 1
        position += 1

    return position

# Get user input
number = int(input("Enter a number: "))
# Find the position of the set bit
result = findSetBit(number)
if result != 0:
    print(f"The position of the set bit in {number} is: {result}")
else:
    print(f"There is no set bit in {number}")