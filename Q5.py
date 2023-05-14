#List in RPN
list=[5,4,"-",9,"*"]
#Empty stack
stack=[]

#Temp variables
A=0
B=0
C=0

#For loop to loop through  RPN list
for x in list:
    #Checks if element is *, if it is, it pops the last two elements and the result is appended to the new stack. 
    if(x=='*'):
        A=stack.pop()
        B=stack.pop()
        C=B*A
        stack.append(C)
        continue
    #Checks if element is /, if it is, it pops the last two elements and the result is appended to the new stack. 
    elif(x=='/'):
        A=stack.pop()
        B=stack.pop()
        C=B/A
        stack.append(C)
        continue
    #Checks if element is +, if it is, it pops the last two elements and the result is appended to the new stack. 
    elif(x=='+'):
        A=stack.pop()
        B=stack.pop()
        C=B+A
        stack.append(C)
        continue
    #Checks if element is -, if it is, it pops the last two elements and the result is appended to the new stack. 
    elif(x=='-'):
        A=stack.pop()
        B=stack.pop()
        C=B-A
        stack.append(C)
        continue
    #If the element is not any of the above, it appends to the new stack with out any calculations.
    else:
        stack.append(x)
        continue

#Prints result
print("Result: ",stack)
