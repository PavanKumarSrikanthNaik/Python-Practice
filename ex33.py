i = 0
numbers = []
a = input("The limit:")
k = input("The  increment:")

def loop(i, numbers, a, k):
	while i < a:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + k
		print "Numbers now: ", numbers

		print"At the bottom i is %d" % i
	return numbers
def loop_for(i, numbers, a):
	for i in range(0, a):
		print "At the top i is %d" % i
		numbers.append(i)
		
		print "Numbers now: ", numbers

		print"At the bottom i is %d" % i
	return numbers

number = loop(i, numbers, a, k)
print "The numbers:"
for num in number:
	print num
for_number = loop_for(i, numbers, a)
print "The numbers:"
for num in for_number:
	print num

