val = int(input("Enter Number : "))
if val % 2 == 0:
    val = val - 1
n = 1
for i in range(0, val):
    print(n)
    n = n + 2
