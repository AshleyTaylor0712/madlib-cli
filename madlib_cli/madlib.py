def game ():
    print("""
    ******************************
    Welcome to 401 Python Madlibs!
    ******************************

    Answer these prompts to make a silly video game premise.

    ********************************************************
    """
    )
game()

word1 = input(" Lets get started! Tell us your favorite color:  ")
word2 = input("Great! Let's keep going. Pass us a creepy animal:  ")
word3 = input("What's your mothers name:  ")
word4 = input("Give us the past tense verb of your favorite hobby ex. biked:  ")
word5 = input("Pass us the name of your favorite character:  ")
word6 = input("Give us a gross adjective:   ")
word7 = input("Whats your favorite food:   ")

def paragraph ():
  print(f"""
  You're building an amazing video game story premise! Check out what you've made so far!
  ************************************************************
  I the {word1} {word2} {word3} have {word4} {word5}'s with sister and plan to steal her {word6} {word7}!
  ************************************************************
  Let's keep going!
  """
  )
paragraph()

word8 = input("What's your favorite giant animal at the zoo:  ")
word9 = input("Name a cute fuzzy animal:  ")
word10= input("Give us a princess name:  ")
word11 = input("Give us a word to describe your personal style:  ")
word12 = input("Give us the plural of your favorite treat:  ")
word13 = input("Give us an adjective to describe your car:  ")
word14 = input("Give us the plural of your favorite item in your home:  ")
word15 = input("Give a number between 1-50:  ")
word16 = input("What's your favorite baby name:  ")
word17 = input("What's your lucky number:  ")
word18 = input("Give us the plural of the last item you purchased:  ")
word19 = input("How many pets do you own:  ")
word20 = input("Give us the plural of the last thing you ate:  ")
def paragraph2 ():
  print(f"""
  You did it! Check out the story you created!
  ************************************************************
  I the {word1} {word2} {word3} have {word4} with {word5}'s sister and plan to steal her {word6} {word7}!

  What are a {word8} and backpacking {word9} to do? Before you can help {word10}, you'll have to collect the {word11} {word12} and {word13} {word14} that open up the {word15} worlds connected to A {word16}'s Lair. There are {word17} {word18} and {word19} {word20} in the game, along with hundreds of other goodies for you to find.
  ************************************************************
  Thanks for playing!
  """
  )
paragraph2()
