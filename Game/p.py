for i in range(1,8):
    for j in range(1,8):
        if(i==1):
            if(j==2 or j==3):
                print("   ",end='') 
            else:
                print(" * " ,end='') 
        elif(i==2 or i==3):
            if(j==1 or j==4):
                print(" * ",end='')
            else:
                print("   ",end='')  
        elif(i==4):
            print(" * ",end='') 
        elif(i==5 or i==6):
            if(j==4 or j==7):
                print(" * ",end='')   
            else:
                print("   ",end='')  
        else:
            if(j==5 or j==6):
                print("   ",end='')
            else:
                print(" * ",end='')                        
    print()                       
        