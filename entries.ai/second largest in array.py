array =[5, 2, 8, 1, 9]

largest=0
second_largest=0
if len(array) < 2:
    print("array elements <2")
for num in array:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)