
def OddOccurring(a):
    N = len(a)
    for x in range(0,N):

        occurrance = 0

        for y in range(0, N):

            if a[x] == a[y]:

                occurrance+=1

             

        if (occurrance % 2 != 0):

            return a[x]

         

        return -1

# Initialize our array
a = []
N = int(input("Enter array size : "))

for i in range(N):
    element = int(input(f"Enter element {i+1}: "))
    a.append(element)
print("\n\nOdd occurring number is : ", OddOccurring(a))