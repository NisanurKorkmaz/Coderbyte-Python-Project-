def NumberReverse(strParam):
  arr=[]
  arr=strParam.split(' ')
  #print(arr)
  l=len(arr)
  s=""
  while(0<l):
    s=s+arr[l-1]+" "
    l=l-1
  return s

# keep this function call here
print NumberReverse(raw_input())
