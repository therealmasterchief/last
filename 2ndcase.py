def Ontime(n):
    iterations=0
    for i in range(1,n+1):
        iterations+=1
    print("when n is ",n,"Iterations=",iterations)

time=int(input("what number would you like to check"))
print(Ontime(time))