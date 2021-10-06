from mypkg import mymod as md

f = open('demo.txt', 'r')

print('access countChars()-->',md.countChars(f))
print('access countLines()-->',md.countLines(f))
print('access test()-->',md.test(f))

# using from to import sections of the module
from mypkg.mymod import test
print('using from to import test() section from mymod -->',test(f))