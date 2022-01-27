def ParallelSums(arr):
  a1=[]
  a2=[]
  toplam=0

  for i in range(len(arr)):
    toplam=toplam+arr[i]
  
  yarisi=toplam/2

  j=0
  while j<(len(arr)):
    a1.append(arr[j])
    a2.append(arr[j+1])
    j=j+2

  t1=0
  for k in range(len(arr)):
    for l in range(len(a1)):
      t1=t1+a1[l]

    a=""
    if t1==yarisi:
      a1.sort()
      a2.sort()
      print(a1,a2)

      if(a1[0]>a2[0]):
        for m in range(len(a1)):
          yedek=a1[m]
          a1[m]=a2[m]
          a2[m]=yedek
        

      for x in range(len(a1)):
        a=a+str(a1[x])+","
      for y in range(len(a2)):
        if y==len(a2)-1 :
          a=a+str(a2[y])
        else :
          a=a+str(a2[y])+","
    
      return a
    else :
      temp=0
      temp=a1[k]
      a1[k]=a2[k]
      a2[k]=temp

    t1=0
  return -1

      


# keep this function call here
print ParallelSums(raw_input())
