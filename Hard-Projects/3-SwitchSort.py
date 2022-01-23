def SwitchSort(arr):
    i=0
    count = 0
    while i< len(arr):
        if arr[i] != i+1 :
            
            while arr[i] != i+1 :
                temp=0
                
                temp= arr[arr[i]-1]
                arr[arr[i]-1]=arr[i]
                arr[i]=temp
                count=count+1
        i=i+1
    return count

print(SwitchSort([1,4,3,2]))
