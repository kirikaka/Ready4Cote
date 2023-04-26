sum=0

while(True):
  for i in range(k):
    if m == 0:
      break
    sum+=a
    m-=1
  if m==0:
    break
  sum+=b
  m-=1

print(sum)