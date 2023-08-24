import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(3001)     #Value commited but not practically proven do not change the value of system provied limits or other

print(sys.getrecursionlimit())
