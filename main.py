# 1.   Write a program that counts lines and characters in a file.
# With your favorite text editor, code a Python module called mymod.py,
# which exports three top-level names:
# a) A countLines(name) function that reads an input file and counts the number of lines in it
# b) A countChars(name) function that reads an input file and counts the number of characters in it
# c) A test(name) function that calls both counting functions with a given input filename.
# All three mymod functions should expect a filename string to be passed in.
# Now, test your module interactively, using import and name qualification to fetch your exports.

from mypkg import mymod as md

f = open('demo.txt','r')
print(f.read())
print(md.countChars(f))
print(md.countLines(f))
print(md.test(f))

# 2. Test your mymod module from Exercise 1 interactively, by using from
# to load the exports directly, first by
# name, then using the from* variant to fetch everything.

from mypkg.mymod import countChars
print('from mymod module importing countChars, the o/p-> ',countChars(f))

from mypkg.mymod import countLines
print('from mymod module importing countLines, the o/p-> ',countLines(f))

from mypkg.mymod import test
print('from mymod module importing test, the o/p-> ',test(f))

from mypkg.mymod import *
# it reads everything like the whole file
print('from mymod module importing everything, the o/p-> ',countChars(f),test(f),countLines(f))


# 3.    Now, add a line in your mymod module that calls the test function automatically only
# when the module is run as a script, not when it is imported The line you add will probably
# test the value of __name__ for the string "__main__", as shown in this unit. Try running your
# module from the system command line;then, import the module and test its functions interactively.

import mypkg.mymod as md
print('for q3--> running test() by importing in main.py---',md.test(f))


# 4.    Write a second module, myclient.py, which imports mymod and tests its functions;
# run myclient from the system command line. If myclient uses from to fetch from mymod,
# will mymod’s functions be accessible from the top level of myclient? --yes(works in pycharm)
# What if it imports with import instead? --> (works using import as well from...)
# Try coding both variations in myclient and test interactively, by importing myclient and inspecting its __dict__.



# 5.  Package imports. Finally, import your file from a package.
# Create a subdirectory  called mypkg nested in a directory on your module import search path,
# move the mymod.py
# module file you created in exercises 1 or 3 into the new directory,
# and try to import it with a package import of the form: import mypkg.mymod.

import mypkg.mymod as md
print('importing mymod from package(mypkg) and running test() ->',md.test(f))

f.close()
print('\n\n')
# 7. Write a Python program to read an entire text file.

f= open('demo1.txt','r')
print(f.read())
f.close()

# 8.  Write a Python program to read first n lines of a file.

print('\n\n')
#n = int(input('enter number of lines to read: '))

f = open('demo1.txt', 'r')
def read_line(f,n):
    line_count = 0
    for i in f.read():
        if(line_count<n and i != '\n'):
            print(i,end ='')
        elif (i == '\n'):
            print()
            line_count += 1
        else:
            break;
    f.close()

#read_line(f,n) # calling the custom read_line function...

# 9. Write a Python program to append text to a file and display the text.

f = open('demo1.txt', 'a+')
#f.write('APPLE,MICROSOFT,GOOGLE,FACEBOOK,NETFLIX')
print(f.read())
f.close()

# 10. Write a Python program to read a file line by line and store it into a list.
f = open('demo1.txt', 'r+')
lines_of_file = f.readlines()
print(type(lines_of_file))
for i in lines_of_file:
    print(i)
f.close()

# 11.  Write a program to print each line of a file in reverse order.
print('\n')
f = open('demo1.txt', 'r+')
lines_of_file = f.readlines()
lines_of_file.reverse()
print(lines_of_file)
f.close()

# 12. Write a Python program to write a list content to a file.
# f = open('demo1.txt', 'w+')
# lines_for_file = ['drake\n','j cole\n',
#                   'french montanna\n','21 savage\n',
#                   'joyner lucas\n', 'big sean\n']
# f.writelines(lines_for_file)
# print(f.read())
# f.close()

# 13. Write a program to compute the number of characters, words and lines in a file.
f = open('demo1.txt', 'r')
print('number of char->',countChars(f))
print('number of lines->',countLines(f))
def count_words(f):

    f.seek(0)
    word_count = 0

    for i in f.read():
       if(i ==' ' or i == '\n' ):
           word_count += 1
    return word_count

print('number of words->',count_words(f))


