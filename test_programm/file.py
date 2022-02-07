
import os

f=open("Test.txt","r")
o=open("Demo.txt","a")
# for line in f.readlines():
#     o.write(line)

o.write(f.read())
