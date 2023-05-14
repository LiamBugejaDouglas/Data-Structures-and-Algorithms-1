#List of numbers.
nums=[1,2,3,4,8,3,1,5,9]
#Temp List.
tempList=[]
#Flag.
bool=False

#Loops in list of numbers.
for i in range(0,len(nums)):
    #Loops in .
    for j in range(0,len(tempList)):
        #Checks if the current value in list of numbers if found in temp list, if found that means its repeated, so it prints the value.
        if(nums[i]==tempList[j]):
            print(nums[i])
            bool=True
            break
    #If value is not found to be repeated it is appended to temp list to be used in more itterations.
    if(bool==False):
        tempList.append(nums[i])