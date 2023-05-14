#List of numbers.
list1=[0,5,3,6,8,7,15,9]
#Empty list to put extreme points.
list2=[]

size=len(list1)

#Loops in list of numbers
for x, item in enumerate(list1):
    #Checks if x is in the last position of the list, if yes it breaks the loop.
    if(x==size-1):
        break
    #Used to skip the first elment of the list.
    elif(x>0):
        #Checks if current item is an extreme point.
        if(list1[x-1] > item < list1[x+1]):
            #Extreme point appended.
            list2.append(item)
        elif(list1[x-1] < item > list1[x+1]):
            #Extreme point appended.
            list2.append(item)
        else:
            continue
    else:
        continue
#Prints extreme point.
print("Extreme points:" ,list2)