import random_word
r=random_word.RandomWords()
print("Welkome to the game Guess the word")
secret_word=r.get_random_word()
letters=[]
lives=len(secret_word)# len () - считает количество букв в слове (длину)
print("You have "+ str(lives) +" lives")
while lives>0:# while lives > 0:  --- повторять игру пока есть жизни0000000000
     got_dash=False
     letter=input("whitch letter will you choose?")
     if letter in letters:
          print("You tried letter "+letter+" Try other!")
          continue
     letters.append(letter)
     for char in secret_word:
          if char in letters:
               print(char,end="  ")
          if char not in letters:
               print("_",end="  ")
               got_dash=True
     print()
     if letter not in secret_word:
          print("your letter is wrong!")
          lives=lives-1
          print("You have lafte "+str(lives)+" lives")
          if lives==0:
               print("game over!The secret word was " + secret_word)
     if got_dash==False:
          print("You win!!!!")
          break

          