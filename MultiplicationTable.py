n = int(input("Enter the multiplication table:"))
m = int(input("Enter how many terms to be generated:"))
for i in range(1,m+1):
    table = n * i
    print(i, 'x', n, '=' ,table)