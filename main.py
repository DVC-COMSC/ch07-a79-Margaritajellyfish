
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])

print ('Sum of rows: ', end=' ')
for i in range(rnum):
	rsum = sum(numbers[i])
	print (rsum, end=' ')
print()

# ******************************
# Make your Code
# ******************************
print ('Sum of columns: ', end=' ')
for j in range(cnum):
    csum = 0
    for k in range(rnum):
        csum += numbers[k][j]
    print (csum, end=' ')