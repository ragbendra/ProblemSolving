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