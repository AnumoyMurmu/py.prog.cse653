#perfect square

count=0

for i in range (1,1001): 
     if(int(i**0.5)**2==1): 
          count+=1;

print (count)