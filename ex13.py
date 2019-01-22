from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "Enter two values:",
a = raw_input()
b = input()
print "The value you entered is: %r" % (int(a) + b)