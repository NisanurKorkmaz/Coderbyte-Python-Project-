def EvenPairs(strParam):

  sayilar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  s1=1
  s2=1

  for i in range(len(strParam)):
    if(strParam[i] in sayilar and strParam[i+1] in sayilar ):
      bir=strParam[i]
      iki=strParam[i+1]
      
      bir=int(bir)
      iki=int(iki)
      
      if bir%2==0 and iki%2==0 :
        return "true"
      elif strParam[i+1] in sayilar and strParam[i+2] in sayilar :
        s1=strParam[i]+strParam[i+1]
        s2=strParam[i+2]
        s1=int(s1)
        s2=int(s2)
        if s1%2==0 and s2%2==0 :
          return "true"
        s1=strParam[i]
        s2=strParam[i+1]+strParam[i+2]
        s1=int(s1)
        s2=int(s2)
        if s1%2==0 and s2%2==0 :
          return "true"
      
