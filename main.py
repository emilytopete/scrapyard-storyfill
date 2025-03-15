'''
ID: 1601658

Project name: Story filler
'''

Black   = '\033[30m'
Red     = '\033[31m'
Green   = '\033[32m'
Yellow  = '\033[33m'
Blue    = '\033[34m'
Magenta = '\033[35m'
Cyan    = '\033[36m'

colors = [Black, Red, Green, Yellow, Blue, Magenta, Cyan]

def operate():
  
  stories = ['1. Dog', '2. Frog', '3. Dinosaur', '4. Milkshake', '5. Living in superhero world']
  fillers = ['verb', 'noun', 'character', 'adjective', 'adverb', 'place to live', 'creature', 'food']
  
  dog_inputs    = []
  frog_inputs   = []
  dino_inputs   = []
  milks_inputs  = []
  super_inputs  = []
  secret_inputs = []

  def dog(speech):
    c1 = input(fillers[2])
    c2 = input(fillers[0])  
    c3 = input(fillers[3])
    c4 = input(fillers[4])
    c5 = input(fillers[1])
    
    dog_inputs.append(c1)
    dog_inputs.append(c2)
    dog_inputs.append(c3)
    dog_inputs.append(c4)
    dog_inputs.append(c5)
    
    print("")
    print (colors[2], "Once there was a dog named", speech[0])
    print (" He loved to go", speech[1])
    print (" Every one always thought he was so", speech[2])
    print (" Everything he did, he did", speech[3])
    print (" He loved", speech[4], colors[0])
  
  def frog(speech):
    d1 = input(fillers[2])
    d2 = input(fillers[5])
    d3 = input(fillers[3])
    d4 = input(fillers[6])
    d5 = input(fillers[4])
    d6 = input(fillers[7])
    d7 = input(fillers[5])
    
    frog_inputs.append(d1)
    frog_inputs.append(d2)
    frog_inputs.append(d3)
    frog_inputs.append(d4)
    frog_inputs.append(d5)
    frog_inputs.append(d6)
    frog_inputs.append(d7)
      
    print("")
    print(colors[1], "A frog named", speech[0], "once lived in a", speech[1])
    print("", speech[0], "loved where he lived and never wanted to leave")
    print(" But one day a", speech[2], speech[3], "came and destroyed his house")
    print(" So he", speech[4], "packed all of his", speech[5])
    print(" and went to live in a", speech[6], colors[0])
  
  def dino(speech):
    e1 = input(fillers[2])
    e2 = input(fillers[0])
    e3 = input(fillers[3])
    e4 = input(fillers[4])
    e5 = input(fillers[7])
    
    dino_inputs.append(e1)
    dino_inputs.append(e2)
    dino_inputs.append(e3)
    dino_inputs.append(e4)
    dino_inputs.append(e5)
    
    print(colors[5], "")
    print("One day", speech[0], "woke up and noticed something different")
    print("he woke up and", speech[1])
    print("but saw out his window a(n)", speech[2], "dinosaur")
    print("he realized he went back in time")
    print("he", speech[3], "ran outside and played with the dinosaur")
    print("he was sad because there was no more", speech[4], colors[0])
  
  def milks(speech):
    f1 = input(fillers[7])
    f2 = input(fillers[4])
    f3 = input(fillers[7])
    f4 = input(fillers[0])
    f5 = input(fillers[7])
    f6 = input(fillers[3])
    f7 = input(fillers[2])
    
    milks_inputs.append(f1)
    milks_inputs.append(f2)
    milks_inputs.append(f3)
    milks_inputs.append(f4)
    milks_inputs.append(f5)
    milks_inputs.append(f6)
    milks_inputs.append(f7)
    
    print(colors[4], "")
    print("Today we are making a custom milkshake")
    print("The first ingredient is", speech[0])
    print("Now lets", speech[1], "mix it in.")
    print("This step is very important")
    print("now our next ingredient is", speech[2])
    print("now lets take a break and", speech[3])
    print("now for our final ingredient", speech[4])
    print("WOW, that is", speech[5])
    print("Thanks for making this ")
    print("now we will take it too our customer", speech[6], colors[0])
  
  def super(speech):
    g1 = input(fillers[2])
    g2 = input(fillers[4])
    g3 = input(fillers[7])
    g4 = input(fillers[6])
    g5 = input(fillers[5])
    
    super_inputs.append(g1)
    super_inputs.append(g2)
    super_inputs.append(g3)
    super_inputs.append(g4)
    super_inputs.append(g5)
    
    print("", colors[0])
    print("Today is just a regular day for", speech[0])
    print("While he was a at work a helicopter", speech[1], "crashed through the wall")
    print(speech[0], "just sat down ate his", speech[2], "and got back to work ")
    print("a little squished since he was sharing his desk with a helicopter wing")
    print("Then, after work", speech[0], "walked home")
    print("and found out a giant", speech[3], "walked over his apartment")
    print("So, he went to his friend's", speech[4])
    print("It was easy for him to sleep becasue of the sounds of crashing and lasers outside")
    print("Just another regular day for", speech[0])
  
  def secret(speech):
    fillers = ['verb', 'noun', 'character', 'adjective', 'adverb', 'place to live', 'creature', 'food']
    #            0       1        2              3           4           5            6           7
    h1 = input(fillers[2])
    h2 = input(fillers[6])
    h3 = input(fillers[2])
    h4 = input(fillers[3])
    h5 = input(fillers[7])
    h6 = input(fillers[4])
    h7 = input(fillers[4])
    
    
    secret_inputs.append(h1)
    secret_inputs.append(h2)
    secret_inputs.append(h3)
    secret_inputs.append(h4)
    secret_inputs.append(h5)
    secret_inputs.append(h6)
    secret_inputs.append(h7)
    
    print("", colors[5])
    print("this is a secret story you have unlocked")
    print("This number is my birth year so here you go")
    print("", colors[0])
    print("There was once a little girl named", speech[0])
    print("she loved her pet", speech[1], speech[2])
    print("she went everywhere with it")
    print("everyone thought the", speech[1], "was so", speech[3])
    print("One day", speech[2], "got sick")
    print(speech[0], "cried all day long")
    print(speech [2], "wouldn't eat", speech[4], "which was her favorite food")
    print(speech[0], speech[5], "hugged her", speech[1])
    print("The next day the ", speech[2], "died")
    print(speech[0], speech[6], "cried for a whole week")
    print("but then wold dream about her pet", speech[1], "and would feel better")
    print(speech[0], "buried her", speech[1], "and left to go get a new one")
    print("THE END")

  def intro():
    print("Choose a story theme and fill in the blanks to write your own story")
    print("")
    print("What story do you want?", colors[1],  "(Use the number)", colors[0])
    print("")
    print(stories[0])
    print(stories[1])
    print(stories[2])
    print(stories[3])
    print(stories[4])
    
    print("")
    global x
    x = input("")
    print("")
  
    if x == "1":
      dog(dog_inputs)
      
    if x == "2":
      frog(frog_inputs)
        
    if x == "3":
      dino(dino_inputs)
      
    if x == "4":
      milks(milks_inputs)
    
    if x == "5":
      super(super_inputs)
    
    if x == "2007":
      secret(secret_inputs)
  
  intro()

operate()

i=0

while i <= 10:
  
  print("")
  print("⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ⋆⁺₊ ")
  print("")
  print("Do you want to write another story? (Y/N) (Capitalize please)")
  print("")
  answer = input("")
  
  if answer == "Y":
    print("")
    print("⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ☾⋆⁺₊⋆⋆⁺₊⋆ ⋆⁺₊ ")
    print("")
    operate()
  
  if answer == "N":
    print("")
    print(colors[5], "♡", colors[4], "ok", colors[5], "♡", colors[0])
    break














