def find_index(symbol, elements): 
  """
  the function looks for the index of the matching element with the array
  """ 
  ind = None
  for (index, elem) in enumerate(elements):
    if symbol == elem:
      ind = index
      break
  return ind