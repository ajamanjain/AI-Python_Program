x=0
y=0
a=4
b=3
count=0
print("WATER JUG PROBLEM ")  
print("Capacity of both the jugs are =(4,3)")
print("Intially jugs are empty = (0,0)")
print("Our goal is to fill j1 jug with 2 litre of water =(2,0)")
while (x!=2 or y!=0):
  r = int(input("Enter rule : "))
  if(r==1):
    x=a
    print(x,y)
    count+=1

  elif(r==2):
    y=b
    print(x,y)
    count+=1

  elif r==3:
    x = x-(b-y)
    y=3
    print(x,y)
    count+=1

  elif r==4:
    y=y-(a-x)
    x=4
    print(x,y)
    count+=1
    
  elif r==5:
    y=x
    x=0
    print(x,y)
    count+=1
    
  elif r==6:
    y=0
    print(x,y)
    count+=1
    
  elif r==7:
    y-=(4-x)
    x=a
    print(x,y)
    count+=1
    
  elif r==8:
    x-=(3-y)
    y=b
    print(x,y)
    count+=1
  
  elif r==9:
    x+=y
    y=0
    print(x,y)
    count+=1
    
  elif r==10:
    y+=x
    x=0
    print(x,y)
    count+=1

  elif x==2 and y==0:
      print("goal achieved")
      print("Total no. of steps taken is:: " ,count)
      break
  
    
