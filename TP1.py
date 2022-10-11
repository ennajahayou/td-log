def factorilel(x):
    if x==1:
      return 1
    else:
        return x*factorilel(x-1)

x=factorilel(2)
print(x)