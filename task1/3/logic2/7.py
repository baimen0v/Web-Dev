def make_chocolate(small, big, goal):
  if goal>=5*big:
    reminder=goal-5*big
  else:
    reminder=goal%5
  if reminder<=small:
    return reminder
  return -1
