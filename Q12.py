#Function which gives the fibonacci sequence.
def fibonacciSeq(num):
    if num<0:
        print("Input too small")
    elif num==0:
        return 0
    elif num<2:
        return 1
    else:
        return fibonacciSeq(num-1) + fibonacciSeq(num-2)

    total=0
    for i in range(0,num):
        total=total+fibonacciSeq(i)
    print(total)

print(fibonacciSeq(10))
