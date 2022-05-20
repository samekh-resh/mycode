from pprint import pprint


#foo = open('frankenstein.txt')


#pprint(foo.readlines())

#you should always close all the files after opening them 
#foo.close()

with open("frankenstein.txt") as x:
    print(x.read())
