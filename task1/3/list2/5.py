def sum67(nums):
  sum=0
  skip=False
  for i in nums:
    if(i==6):
      skip=True
    elif(i==7 and skip):
      skip=False
    elif skip==False:
      sum+=i
  return sum
