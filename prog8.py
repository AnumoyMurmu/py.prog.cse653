#perfect fifth power

count=0

for i in range (1,1001):
      cc=round(i** (1/5))
      if cc**5==i:
          print (1)
          count+=1

print("total perfect cube:", count)