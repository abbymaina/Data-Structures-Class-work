numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]
key = 77


found = False
for num in numbers:
    if num == key:
        print("Found")
        found = True
        break
else:
    print("Not Found")


start = 0
end = len(numbers) - 1
found = False

while start <= end:
    mid = (start + end) // 2
    if numbers[mid] == key:
        print("Found element at position:", mid)
        found = True
        break
    elif key < numbers[mid]:
        end = mid - 1
    else:
        start = mid + 1

if not found:
    print(f"{key} not found in the list")