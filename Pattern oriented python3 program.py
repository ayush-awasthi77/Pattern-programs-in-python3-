# triangle pattern code
n = int(input("enter number of side"))
org = n
for i in range (1,n+1):
     print('*'* i)
print("     ")
# square pattern code
for a in range(n):
    print('*'* n)
print("     ")
# rectangle pattern code
h = int(input("enter a height"))
for b in range(h):
  print('&'*n)
print("      ")
# inverted right angle triangle
for i in range(n,0,-1):
    print('*'* n)
    n = n-1
print("     ")
# pyramid pattern code
n = org
for i in range (1,n+1):
    space = ' '* (n-i)
    stars = '*'*(2*i -1)
    print (space+ stars)
print("     ")



