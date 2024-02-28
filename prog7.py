#perfect cube

count=0

for i in range (1,1001):

      cc=round(i**(1/3))
      if cc**3==i:
          count+=1
          print (i)

print("total perfect cube:", count)