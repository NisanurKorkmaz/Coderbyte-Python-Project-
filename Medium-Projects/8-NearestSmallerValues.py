def NearestSmallerValues(arr):
  newarr=[]
  flag=0
  l=len(arr)
  for i in range(l):
    if(i==0):
      newarr.append("-1")

    elif(arr[i]<arr[i-1]):
      j=i-1
      while(-1<j):
        if(arr[i]>arr[j] or arr[i]==arr[j]):
          newarr.append(arr[j])
          flag=1
          break
        j=j-1
      if(flag==0):
        newarr.append("-1")

    elif(arr[i]>=arr[i-1]):
      newarr.append(arr[i-1])
    
    s=""
    for k in range(len(newarr)):
      s=s+str(newarr[k])+" "

  return s

# keep this function call here
print NearestSmallerValues(raw_input())
