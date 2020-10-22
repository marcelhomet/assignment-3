x = int(input("Enter a value: "))
i = 1
y = 0
while( i <= x ):	
	n = x % i
	if n == 0:
		y = y + i
	i = i + 1
if y == x + 1:
	print("es primer")
else:
	print("no es primer")	