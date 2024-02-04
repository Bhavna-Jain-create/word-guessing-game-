import random
wordList = ["custom","where","love","for","hate","great"]
words = random.choice(wordList)
#print(words)
guess = ''
turns = 10
while turns > 0:
   failed = 0
   for char in words:
     if char in guess:
      print(char)
     else:
      print("_")
      failed += 1
      #print(failed)
   if failed == 0:
     print("You won")
     break
   userLetter = input("Guess another character:")    
   guess += userLetter 
   if userLetter not in words:
     turns -= 1
     print(f"You have only {turns} chances")
   if turns == 0:
     print("You lose")
     print(words)  
   

   
