from sys import argv

script, filename = argv

print "Let's read what's written into %r" % filename
target = open(filename)
print target.read()