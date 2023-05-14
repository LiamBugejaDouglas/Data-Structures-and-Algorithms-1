#Function which returns an approximation of the sqaure root of a number using the Newton-Raphson Method.
#In the function it loops for 10 times.
def newtonsMethod(num, reps=10):
    cons= float(num)
    for i in range(reps):
        num = (num+(cons/num))/2
    return num

print(newtonsMethod(2))

