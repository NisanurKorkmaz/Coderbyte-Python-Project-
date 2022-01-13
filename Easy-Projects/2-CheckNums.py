def ChecksNums(num1,num2):
    if num1<num2:
        return True
    elif num2<num1:
        return False
    else:
        return -1

print(ChecksNums(33,98))
