
'''
Given two strings word and anagram, return true if anagram
is an anagram of word, and false otherwise.
'''    
def isAnagram(word, anagram):
  # break early for no-input  
  if len(word) <= 0 and len(anagram) <= 0:
    return False

  # break early for mis-matched length
  if len(word) != len(anagram):
    return False

  # break early if same word passed in
  if word.lower() == anagram.lower():
    return False  

  # sorted strings should match
  if ''.join(sorted(word.lower())) == ''.join(sorted(anagram.lower())): 
    return True 
  else:
    return False   

if __name__ == '__main__':
  word = input("Type a word:")
  anagram = input("Type an anagram:")
  print(f"\nIs {anagram} an anagram of {word}? {isAnagram(word,anagram)}\n")
