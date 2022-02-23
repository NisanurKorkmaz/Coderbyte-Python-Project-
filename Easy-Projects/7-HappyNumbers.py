def HappyNumbers(num):

  s=str(num)
  toplam=0
  for i in range(len(s)):
    sayi=int(s[i])
    toplam=toplam+sayi

  if(toplam==1):
    return "true"
  else:
    return "false"

# keep this function call here
print HappyNumbers(raw_input())
