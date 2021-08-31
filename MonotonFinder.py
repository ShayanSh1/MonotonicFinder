user_array = list()

def is_monotonic(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)): 
        return "Monotone Increasing" 
    elif all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return "Not Monotonic Array"

size = int(input("Enter the size of the array : "))

for i in range(size):
    n = int(input("Enter value for position {} : ".format(i)))
    user_array.append(n)

print("Input array is " + str(is_monotonic(user_array)))

#first input the size of array (for example 10) , then input the value's in the array
#enter and get the answer , enjoy it <3