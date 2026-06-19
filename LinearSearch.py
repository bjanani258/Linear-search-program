a = [1,2,3,4,5,6,7,8,9]
target = int(input("Enter target: "))

found = False
for i in range(len(a)):   # loop over indices
    if a[i] == target:    # check value at index
        print("Element Found at index", i)
        found = True
        break

if not found:
    print("Not Found")
