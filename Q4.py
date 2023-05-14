import random
def distinct(list):
    #Loops four times to compare each possibility
    for i in range(len(list)):
        for j in range(len(list)):
            for k in range(len(list)):
                for l in range(len(list)):
                    #Checks  a * b = c * d and a ≠ b ≠ c ≠ d
                    if (list[i] != list[j] and list[i] != list[k] and
                            list[i] != list[l] and list[j] != list[k] and
                            list[j] != list[l] and list[k] != list[l] and
                            list[i] * list[j] == list[k]  * list[l]):

                        print(list[i], " x ", list[j], " =", list[k], " x ", list[l])

A=[]
#Inputting random numbers in a list.
for x in range(10):
    A.append(random.randint(0, 40))
#Prints the list.
print(A)
#Prints all possibilties.
distinct(A)
