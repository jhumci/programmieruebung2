# Comments
with open("data/primes.txt","w") as fo:
    for n in range (x,y):
        if all(n%i!=0 for i in range (2,n)):
            a=[]
            a.append(n)             
            print (">>>Writing the values to primes.txt...")
            print ("##########Calculated by my prime calculator##########", file = fo)
            print ("", file = fo)
            print ((a), file = fo)
