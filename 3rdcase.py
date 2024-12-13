def ONsquareTime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
            iteration+=1
        print("")
    print("\n when n is ",n," Iterations= ",iteration,"\n")

time=int(input("waht number would you like to check"))
ONsquareTime(time)