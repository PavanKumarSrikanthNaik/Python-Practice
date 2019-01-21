print "How old are you ?",
age = input() #interprets it as a value
print "How tall re you?",
height = raw_input() #interprets it as a string
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "Enter the values to be added.", 
a = input()
b = input()
total = a + b
print "The sum of %r and %r is %r " % (a, b, total)
