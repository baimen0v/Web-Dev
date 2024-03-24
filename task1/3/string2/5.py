def end_other(a, b):
 newa=a.lower()
 newb=b.lower()
 if(newa.endswith(newb) or newb.endswith(newa)):
  return True
 else:
  return False
  
