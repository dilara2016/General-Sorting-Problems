def rotations(a,n,a_size):
    for i in range(n):
        rotate(a,a_size)

def rotate(a,a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i+1]
    a[a_size-1] = temp

def printArray(a,a_size):
    for i in range(a_size):
        print("% d"% a[i], end=" ")
    print("\n")

a = []
a_size = int(input("Length of array: "))
for i in range(a_size):
    element = int(input("Element: "))
    a.append(element)
printArray(a,len(a))
rotations(a,2,len(a))
printArray(a,len(a))