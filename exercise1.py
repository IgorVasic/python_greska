"""
s = "flask"

print(s[0])
print(s[3])
print(s[2::])
print(s[1:4])
print(s[-1])
print(s[::-1])

l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print(l)
"""

#d1 = {'simple_key':'hello'}
#d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#x = d2['k1']['k2']
#print(x)
x2 = d3['k1'][0]['nest_key'][1][0]
print(x2)
mylist = [1,1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))
age = 4
name = 'Sammy'

print("Hello my dog's name is {} and he is 4 years old ".format(name,age))











