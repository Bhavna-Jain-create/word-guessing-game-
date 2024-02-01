import random
wordList = ["custom","where","love","for","hate","great"]
words = random.choice(wordList)
#print(words)
guesses1 = ''
turns = 10
while turns > 0:
   failed = 0
   for char in words:
     if char in guesses1:
      print(char)
     else:
      print("_")
      failed += 1
      #print(failed)
   if failed == 0:
     print("You won")
     break
   userLetter = input("Guess another character:")    
   guesses1 += userLetter 
   if userLetter not in words:
     turns -= 1
     print(f"You have only {turns} chances")
   

   
