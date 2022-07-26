str = 'the quick brown fox jumps over the lazy dog.'

def word_count(str): 
  counts = dict() # create blank dictionary
  words = str.split()  # split up into individual words using string method
  
  for word in words: # use for loop to check word occurrences
      if word in counts: 
        counts[word] += 1 #increment key value by one is=f the word occurs
      else: counts[word] = 1 # else word occurrence is equal to 1
  return counts # return updated dictionary once words have been checked

print(word_count(str))

