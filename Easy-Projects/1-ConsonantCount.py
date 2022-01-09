def ConsonantCount(strParam):
  count = 0
  liste = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","w","v","y","z"]
  strParam = strParam.lower()
  for i in strParam:
    if i in liste:
      count = count + 1
  # code goes here
  return count

# keep this function call here
print ConsonantCount(raw_input())
