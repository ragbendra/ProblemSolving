"""# No Duplicates
list1 = [0, 23,43, 2, 12, 27]
print("The Unsorted list is: ", list1)
for i in range(len(list1)-1):
    min_val = min(list1[i:])
    min_index = list1.index(min_val)
    list1[i], list1[min_index] = list1[min_index], list1[i]
    print(f"The {i} position sorted list1 is: ",list1)

print("\n")

# Duplicates
list2 = [3,2,2,3,1,0,5,3,9,8,5,4,7,6]
print("The unsorted list is: ", list2)
for i in range(len(list2) - 1):
    min_val = min(list2[i:])
    min_index = list2.index(min_val, i)
    if list2[i] != list2[min_index]:
        list2[i], list2[min_index] = list2[min_index], list2[i]
    print(f"The {i} position sorted list2 is: ", list2)

print("\n")"""

# User Input
num = int(input("Enter how many numbers you want in the list: "))
list3 = [int(input("Enter the number: ")) for n in range(num)]
print("The unsorted list is: ", list3)
for i in range(len(list3) - 1):
    min_ind = i
    for j in range(i+1, len(list3)):
        if list3[j] < list3[min_ind]:
            min_ind = j
    if list3[i] != list3[min_ind]:
        list3[i], list3[min_ind] = list3[min_ind], list3[i]
    print(f"The {i} position sorted list is: ",list3)
