from itertools import permutations


def balanceable(numbers):
    a = sum(numbers)
    perm = list(permutations(numbers))
    #for i in list(perm):
        #print(i)

    for eachlist in perm:
        currentsum = 0
        for number in eachlist:
            if number == a/2:
                print("Function is balanceable")
                return True
            else:
                currentsum += number
            if currentsum == a/2:
                print("Function is balanceable")
                return True
    print("Function is not balanceable")
    return False


#enter numbers here separated by commas
balanceable([1,2,3,4])

