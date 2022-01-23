def LetterCount(strParam):

  strParam=strParam.lower()

  max=1
  greatest=""

  arr=strParam.split(" ")
  l=len(arr)

  for i in range(l):
    word = arr[i]
    for j in range(len(word)):
      occurence=word.count(word[j])
      
      if(occurence>max):
        max=occurence
        print(max)
        greatest=word
            
  if max == 1 :
    return -1
  return greatest

# keep this function call here
print LetterCount("Hello apple pie")
