num=17

halfNum=num/2

#Function checks if number is prime
if num>1:
        #Loops through half of the number, example if 50 is given it loops through 1-25
        for i in range(2,int(halfNum+1)): 
                #If it finds a number that when divided by the input gives a modulus=0 it means the number is not prime.
                if(num%i)==0:
                        print("Number given is not prime")
                        break
        else:
                #If it loops through and does not find any modulus=0 it means the number is prime
                print("Number is prime")

#Sieve of Eratosthenes.
prime = [True for i in range(num+1)]
p = 2
print("All prime numbers under the number given: ")
while (p * p <= num):
        if (prime[p] == True):
                for i in range(p * p, num+1, p):
                        prime[i] = False
        p += 1

for p in range(2, num+1):
        if prime[p]:
            print(p)
