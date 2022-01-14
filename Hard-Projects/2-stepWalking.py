def stepWalking(num) :
    if num==1 :
        return 1
    if num==2 :
        return 2
    return stepWalking(num-1) + stepWalking(num-2)

print(stepWalking(3))
