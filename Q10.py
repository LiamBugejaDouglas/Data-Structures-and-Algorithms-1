#Function which finds largest num.
def maxNum(nums, size):
    #If list has only one element it returns that element.
    if(size==1):
        return nums[0]
    else:
        #Recursively finds the largest number.
        return max(nums[size-1], maxNum(nums,size-1))

#List of numbers.
nums=[1,6,2,6,7,19,54,21,-12]
#Size of list.
size=len(nums)
#Class function and print output.
print(maxNum(nums, size))