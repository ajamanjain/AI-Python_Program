m1 = 3  # int(input("Enter the number of the missionary: "))
c1 = 3  # int(input("Enter the number of the Cannibal: "))
m2 = 0
c2 = 0
print("Intially m&c at bank 1: ")
print(m1, c1)
print("Intially m&c at bank 2: ")
print(m2, c2)
# place1=[m1,c1]
# place2=[m2,c2]
# print(place1)
# print(place2)
while(1):
    r = int(input("Enter rule no.: "))
    if(r == 1):
        m1 -= 1
        c1 -= 1
        m2 += 1
        c2 += 1
        print("when 1m and 1c goes from bank1 to bank 2")
        print("bank1:")
        print(m1, c1)
        print("bank2:")
        print(m2, c2)
    elif(r == 2):
        m1 -= 1
        m2 += 1
        print("when 1m goes from bank1 to bank 2")
        print("bank1:")
        print(m1, c1)
        print("bank2:")
        print(m2, c2)
    elif(r == 3):
        c1 -= 1
        c2 += 1
        print("when 1c goes from bank1 to bank 2")
        print("bank1:")
        print(m1, c1)
        print("bank2:")
        print(m2, c2)
    elif(r == 4):
        m1 -= 2
        m2 += 2
        print("when 2m goes from bank1 to bank 2")
        print("bank1:")
        print(m1, c1)
        print("bank2:")
        print(m2, c2)
    elif(r == 5): 
        c1 -= 2
        c2 += 2
        print("when 2c goes from bank1 to bank 2")
        print("bank1:")
        print(m1, c1)
        print("bank2:")
        print(m2, c2)
    elif(r==6): #
        m1+=1
        c1+=1
        m2-=1
        c2-=1
        print("when 1m and 1c goes from bank2 to bank1")
        print("bank1:")
        print(m1,c1)
        print("bank2:")
        print(m2,c2)
    elif(r==7):#
        m1+=1
        m2-=1
        print("when 1m goes from bank2 to bank1")
        print("bank1:")
        print(m1,c1)
        print("bank2:")
        print(m2,c2)
    elif(r==8):#
        c1+=1
        c2-=1
        print("when 1c goes from bank2 to bank1")
        print("bank1:")
        print(m1,c1)
        print("bank2:")
        print(m2,c2)
    elif(r==9):#
        m1+=2
        m2-=2
        print("when 2m goes from bank bank2 to bank1")
        print("bank1:")
        print(m1,c1)
        print("bank2:")
        print(m2,c2)
    elif(r==10):#when 2c goes from bank1 to bank 2
        c1+=2
        c2-=2
        print("when 2c goes from bank2 to bank1")
        print("bank1:")
        print(m1,c1)
        print("bank2:")
        print(m2,c2)
    if(m2==3 and c2==3):
        break
    


print("FINALLY M&C at BANK1 : ")
print(m1,c1)
print("FINALLY M&C at BANK2 : ")
print(m2,c2)



# Answer: 1,7,5,8,4,6,4,8,5,8,5
