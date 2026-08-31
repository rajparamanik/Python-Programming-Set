# this is a simple loop example in Python

for i in range(10): # This will loop from 0 to 9
    print("I love you")  # This will print the current value of i in each iteration


arr = [1, 2, 3, 4, 5] # This is a list of numbers
for i in arr:
    print(i) # This will print the current value of i in each iteration


n = int(input("Enter a number: ")) # This will take input from the user
Arr1 = [0] * n # This will create a list of size n
for i in range(n): # This will loop from 0 to n-1
    Arr1[i] = int(input("Enter a number: ")) # This will take input from the user in each iteration
for i in range(n): # This will loop from 0 to n-1
    print(Arr1[i]) # This will print the current value of Arr1 in each iteration


# nested loop example in Python
for i in range(3): # This will loop from 0 to 2
    for j in range(3): # This will loop from 0 to 2
        print(i, j) # This will print the current value of i and j in each iteration



# star pattern example in Python
n = 5 # This is the number of rows
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()


# triangle pattern in middle example in Python
n = 5 # This is the number of rows
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()


