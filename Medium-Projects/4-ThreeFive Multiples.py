def ThreeFiveMultiples(num):
  toplam=0

  for i in range(1,num):
    if i%3==0:
      toplam=toplam+i
    elif i%5==0:
      toplam=toplam+i

  return toplam

# keep this function call here
print ThreeFiveMultiples(raw_input())
