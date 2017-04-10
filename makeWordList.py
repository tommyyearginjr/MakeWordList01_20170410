#!/usr/bin/python3

mylist=[]

my_string = "blah, lots  ,  of ,  spaces, here!!! "

remove = ";!"

for char in remove:
    my_string = my_string.replace(char, " ")

my_string = ''.join(my_string.split())
my_string = my_string.split(',')

for x in my_string:
    mylist.append(x)

f = open('wordlist.txt', 'a')
for i in mylist:
    f.write(i+'\n')
f.close()

print(mylist)
