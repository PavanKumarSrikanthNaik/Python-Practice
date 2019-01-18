#Basic formatting
#Simple positional formatting is probably the most common use-case. Use it if the order of your arguments is not likely to change and you only have very few elements you want to concatenate.
#Since the elements are not represented by something as descriptive as a name this simple style should only be used to format a relatively small number of elements.
print "%s %s" % ('one', 'two')
print "{} {}" .format('one', 'two')
print "%d %d" % (1, 2)
print "{} {}" .format(1, 2)
print "{1} {0}" .format('one', 'two')
print "{1} {0}" .format(1, 2)


#Value conversion
class Data (object):
	def __str__(self):
		return 'str'
	def __repr__(self):
		return 'repr'
print "%s %r" % (Data(), Data())
print "{0!s} {0!r}" .format(Data())

#Padding and aligning strings
print "%10s" % ('test')
print "%-10s" % ('test')
print "{:>10}" .format('test')
print "{:10}" .format('test')
print "{:_<10}" .format('test') #able to choose the padding character
print "{:^10}" .format('test') #center align values
print "{:^6}" .format('zip') #When using center alignment where the length of the string leads to an uneven split of the padding characters the extra character will be placed on the right side


#Truncating long strings
print "%.5s" % ('xylophone')
print "{:.5}" .format('xylophone')

#Combining truncating and padding
print "%10.5s" % ('xylophone')
print "{:^10.5}" .format('xylophone')

#numbers
print "%d" % (42)
print "{}" .format(42)
print "%f" % (3.141592653589793)
print "{}" .format(3.141592653589793)

#padding numbers
print "%4d" % (42)
print "{:4}" .format(42)
print "%6.2f" % (3.141592653589793)
print "{:06.2f}" .format(3.141592653589793)

#signed numbers
print "%d" % (42)
print "%d" % (-42)
print "{: d}" .format(23)  
print "{:d}" .format(-23)
print "{:=5d}" .format(-23)
print "{:=+5d}" .format(23)
print "{:+5d}" .format(23)










