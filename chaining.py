class clist(list): #added chaining map and filter to list
  def __init__(self,x):
    if type(x) is list:
      super().__init__(x)
    else:
      super().__init__(list(x))
  def map(self,f):
    return clist(f(x) for x in self)
  def filter(self,f):
    return clist(x for x in self if f(x))

