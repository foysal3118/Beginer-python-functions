def getfib(a,b,n):
    if n==1 :
      print(a)
      return
    if n<1 :
      return
    if n==2 :
      print(a)
      print(b)
      return
    print(a)
    print(b)
    for i in range(3, n+1 ,1):
      c = a+b
      print(c)
      a = b
      b = c
    return
    print(c)
a= int(input())
b = int(input())
c = int(input())
getfib(a,b,c)