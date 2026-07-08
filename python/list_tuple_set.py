# list = []
# tuple = ()
# set = {}

t=6,8,9
print(type(t))

s={}
print(type(s))

print("===========1th question============")

l=[9,0,76,0,8,8]
# how to remove duplicates from list
l=set(l) # set is not to allow duplicates values
print(l)

print("===========2th question============")

s= {89,90,6,"p",788888888,4556,9,(8,88)} # set is allow only tuples in it 
# set is not allow the indexing and slicing
print(s)

v=[89,90,6,"p",788888888,4556,9,(8,88)]
v[0]=9
# tuples are immutable
print(v)

print("===========3th question============")
t={9,9,0}
# tow ways to add values in set
# 1st this 
t.add(8) # wan the add only one value than use this 
# 2nd this
t.update([6,5,4]) # wan the add multiple values than use this 
print(t)


print("===========4th question============")
a = {9,8,7,6,5,4,3,2,1}
# i want to remove the values from set
# 1th type 
a.remove(9) # if the value is not present in set than it will give error
# if the value is not present in set than it will give error

# 2th type to use 
a.discard(9) # if the value is not present in set than it will not give error
# if the value is not present in set than it will not give error
print(a)

print("===========5th question============")

b={9,8,7,6,5,4,3,2,1}
b.pop() # it will remove the random value from set
# if pop values is not add than pop is remov the last value from set
print(b)

