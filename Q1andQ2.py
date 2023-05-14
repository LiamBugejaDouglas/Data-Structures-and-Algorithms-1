import random

#Initialise two empty lists.
list1=[]
list2=[]

#Input random numbers using randint into the lists.
for x in range(0,150):
    y=random.randint(0,1024)
    list1.append(y)

for x in range(0,140):
    y=random.randint(0,1024)
    list2.append(y)

print(list1)
print(list2)

#Creation of Shell Short algorithm.
def shellSort(array, n):

    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

#Creation of Quick Sort algorithm.
def partition(arr, low, high):
    i = (low-1)        
    pivot = arr[high]     
  
    for j in range(low, high):
  
        if arr[j] <= pivot:
  
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

#Inputting the random generated numbers list to the Shell Sort and Quick Sort algorithm.
shellSort(list1,len(list1))
quickSort(list2,0,len(list2)-1)

#Printing the sorted lists.
print("Shell sort: ", list1)
print("Quick sort: ", list2)

#Length of lists
len1=len(list1)
len2=len(list2)

final=[]

a=0
b=0

#Checks that the current iteration is not larger than a list1 and list2.
while (a < len1) and (b <len2):
    #Checks which element is smaller and appends it to the a new list, the smaller elment is incremented.
    if(list1[a]<list2[b]):
        final.append(list1[a])
        a=a+1
    else:
        final.append(list2[b])
        b=b+1

#Prints merged lists.
print("Merged lists: ",final)