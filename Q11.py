import math

#Function which finds the cosin value of a taylor series.
def cos(num, terms):
    cosApprox=0
    #Function loops to have a more accurate approximation.
    for x in range(terms):
        #Cosin function of the taylor series.
        cosApprox += ((-1)**x)*((num**(2*x))/(math.factorial(2*x)))
    return cosApprox

#Function which finds the sin value of a taylor series.
def sin(num, terms):
    sinApprox=0
    #Function loops to have a more accurate approximation.
    for x in range(terms):
        #Sin function of the taylor series.
        sinApprox += ((-1)**x)*((num**((2*x)+1)))/(math.factorial((2*x)+1))

#Value given in radians.
radians1 = math.radians(45)
radians2 = math.radians(80)

#Prints values
print(cos(radians1,5))
print(sin(radians2,5))
