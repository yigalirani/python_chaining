import chaining
l=chaining.clist(range(10))
ans=l.filter(lambda x: x%2).map(lambda x:x*10)
print(ans)
  