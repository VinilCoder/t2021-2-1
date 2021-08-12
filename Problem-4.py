list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = list(())
number = int(input("Enter Number of Elements : "))
for k in range(0, number):
    value = int(input())
    list2.append(value)
print("Given List Item Is : " + str(list2))
dictItem = dict(())
for i in range(len(list1)):
    count = 0
    for j in range(len(list2)):
        if list2[j] % list1[i] == 0:
            count = count + 1
    dictItem.update({i + 1: count})
print("The Dictionary Items are : " + str(dictItem))
