def SimpleEvens(num):
  s=str(num)
  for i in range(len(s)):
    sayi=int(s[i])
    if sayi%2!=0:
      return "false"

  return "true"

# keep this function call here
print SimpleEvens(raw_input())
