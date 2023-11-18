
##### Method 1
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)

##### Method 2
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)

##### Method 3
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')
for x in arr:
    if x < arrMin:
        arrMin = x
print(arrMin)