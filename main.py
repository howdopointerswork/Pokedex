from PIL import Image
from replit import audio



###################################################
################### Bugs ##########################
###################################################


#No bugs yet...


###################################################
###################################################
###################################################


class Pokemon: #Pokemon class

  type1 = "None" #First type

  type2 = "None" #Dual Type

  name = "None" 

  hp = 0 

  spd = 0

  atk = 0

  dfs = 0

  spatk = 0

  spdfs = 0

  #Constructor
  def __init__(self,t1, t2, n, h, a, d, sa, sd, s):

    self.type1 = t1
    self.type2 = t2

    self.name = n
    self.hp = h
    self.spd = s
    self.atk = a
    self.dfs = d
    self.spatk = sa
    self.spdfs = sd

###################################################
###################################################
###################################################

#types = ["None","Normal", "Fire", "Water", "Grass", "Electric", "Fighting", "Psychic", "Dark", "Steel", "Flying", "Ice", "Bug", "Poison", "Ground", "Rock", "Ghost", "Dragon"]


def checkName(p):

  print(p.name)







###################################################
###################################################




def weakness(type1, type2): #function for weakness

#May rework
  match type2:

    case "None": #If no dual type

      match type1:

        case "Normal": #Normal/None

          print(" Fighting\n")

        case "Fire": #Fire/None

          print(" Water\n", "Ground\n", "Rock\n")

        case "Grass": #Grass/None

          print(" Fire\n", "Ice\n", "Flying\n", "Poison\n", "Bug\n") 
          
        case "Water": #Water/None

          print(" Grass\n", "Electric\n")

        case "Electric": #Electric/None

          print(" Ground\n") 

        case "Psychic": #Psychic/None

          print(" Dark\n", "Bug\n", "Ghost\n")

        case "Dark": #Dark/None

          print(" Fighting\n", "Bug\n")

        case "Steel": #Steel/None

          print(" Fire\n", "Fighting\n", "Ground\n")

        case "Fighting": #Fighting/None

          print(" Psychic\n", "Flying\n")

        case "Ground": #Ground/None

          print(" Water\n", "Grass\n", "Ice\n")

        case "Rock": #Rock/None

          print("Grass\n", "Water\n", "Fighting\n", "Steel\n", "Ground\n")

        case "Poison": #Poison/None
          
          print(" Psychic\n", "Ground\n")

        case "Flying": #Flying/None
          
          print(" Electric\n", "Ice\n", "Rock\n")

        case "Bug": #Bug/None
          
          print(" Rock\n", "Flying\n", "Fire\n")
        
        case "Ice": #Ice/None
           print(" Rock\n", "Fire\n", "Steel\n", "Fighting\n")

        case "Dragon": #Dragon/None
           
          print(" Dragon\n", "Ice\n")
           
        case "Ghost": #Ghost/None
          
          print(" Ghost\n", "Dark\n")
          

  

    case "Normal": #Dual type is Normal

      match type1:

        case "Fire": #Fire/Normal

           print(" Water\n", "Fighting\n", "Ground\n", "Rock\n")

        case "Water": #Water/Normal
  
          print(" Grass\n", "Electric\n", "Fighting\n")

        case "Grass": #Grass/Normal

          print(" Fire\n", "Flying\n", "Ice\n", "Bug\n", "Poison\n")










#Checklist for types

#___/Normal type:
                
#Normal - N/A
#Fire - Y
#Water - Y
#Grass - Y
#Electric - N
#Psychic - N
#Dark - N
#Steel - N
#Fighting - N
#Ground - N
#Rock - N
#Poison - N
#Flying - N
#Ice - N
#Dragon - N
#Ghost - N
#Bug - N




      
###################################################
###################################################




def display(i):

  if i<10:
    aud = audio.play_file("cries/00"+str(i)+".wav") 

  elif i<100:
    aud = audio.play_file("cries/0"+str(i)+".wav")

  elif i>=100:
    aud = audio.play_file("cries/"+str(i)+".wav") 
  

  if i<10:
    img = Image.open("gifs/00"+str(i)+".gif") 

  elif i<100:
    img = Image.open("gifs/0"+str(i)+".gif")

  elif i>=100:
    img = Image.open("gifs/"+str(i)+".gif")  
  
  img.show()





###################################################
###################################################





def checkStats(p): #function for checking stats

  #Variable names:
  # atk 
  # dfs
  # spatk 
  # spdfs
  # spd

  #Print each one in order (top-bottom)
  #Copy the code below and paste below it. Replace "HP:" in the new one with whichever stat (Attack, Sp. Atk, Speed, etc.)
  #Replace the second parameter (p.hp) in the pasted one to p.each of the variable names
  
  print(" HP:", p.hp)
  print(" Attack:", p.atk)
  print(" Defense:", p.dfs)
  print(" Special Attack:", p.spatk)
  print(" Special Defense:", p.spdfs)
  print(" Speed:", p.spd)
  
  
  
  




  #Also print the total
  t = 0
  # And t should equal the sum of all the stats
  
  # ADD LINE FOR SUMMING HERE


  t += (p.hp + p.atk + p.dfs + p.spatk + p.spdfs + p.spd)
  # Uncomment the line below by deleting the #
  print(" Total:", t, "\n")

  

###################################################
###################################################

def checkEntry(p):
 

  
  checkName(p)

  print(" Type:", p.type1, "/", p.type2, "\n\n\n\n")

  print(" Stats:\n")
  checkStats(p)

  print("\n")
  print("\n")

  print(" Weaknesses:\n")
  weakness(p.type1, p.type2)

  #add new functions 










         



###################################################
###################################################

###################################################
###################################################
########## Main function / Testing ################
###################################################
###################################################


###################################################
########### Declarations / Assignments ############
###################################################


types = ["None","Normal", "Fire", "Water", "Grass", "Electric", "Fighting", "Psychic", "Dark", "Steel", "Flying", "Ice", "Bug", "Poison", "Ground", "Rock", "Ghost", "Dragon"]

flag = False
switch = True


#Put each pokemon in here, so we can use the array and dex number ~B-)>

#Space before every name

natDex = [" None", " Bulbasaur", " Ivysaur", " Venusaur", " Charmander", " Charmeleon", " Charizard", " Squirtle", " Wartortle", " Blastoise", " Caterpie", " Metapod", " Butterfree", " Weedle"]


###################################################
############ Make Pokemon Here ####################
###################################################

#--------------------------------------------------#

#Use types[n] for the first and second parameters:


#  n = 0    None

#  n = 1    Normal

#  n = 2    Fire

#  n = 3    Water

#  n = 4    Grass

#  n = 5    Electric

#  n = 6    Fighting

#  n = 7    Psychic

#  n = 8    Dark

#  n = 9    Steel

#  n = 10   Flying

#  n = 11   Ice

#  n = 12   Bug

#  n = 13   Poison

#  n = 14   Ground

#  n = 15   Rock

#  n = 16   Ghost 

#  n = 17   Dragon


#--------------------------------------------------#


bulbasaur = Pokemon(types[4], types[0], natDex[1], 45, 49, 49, 65, 65, 45)

ivysaur = Pokemon(types[4], types[13], natDex[2], 60, 62, 63, 80, 80, 60)

venusaur = Pokemon(types[4], types[13], natDex[3], 80, 82, 83, 100, 100, 80)

charmander = Pokemon(types[2], types[0], natDex[4], 39, 52, 43, 60, 50, 65)

charmeleon = Pokemon(types[2], types[0], natDex[5], 58, 64, 58, 80, 65, 80)

charizard = Pokemon(types[2], types[10], natDex[6], 78, 84, 78, 109, 85, 100)

squirtle = Pokemon(types[3], types[0], natDex[7], 44, 48, 65, 50, 64, 43)

wartortle = Pokemon(types[3], types[0], natDex[8], 59, 63, 80, 65, 80, 58)

blastoise = Pokemon(types[3], types[0], natDex[9], 79, 83, 100, 85, 105, 78)

caterpie = Pokemon(types[12], types[0], natDex[10], 45, 30, 35, 20, 20, 45)

metapod = Pokemon(types[12], types[0], natDex[11], 50, 20, 55, 25, 25, 30)

butterfree = Pokemon(types[12], types[10], natDex[12], 60, 45, 50, 90, 80, 70)

weedle = Pokemon(types[12], types[13], natDex[13], 40, 35, 30, 20, 20, 50)










###################################################
########### Add Each Pokemon To Dex ###############
###################################################


dex = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, caterpie, metapod, butterfree, weedle]




###################################################
############## Function Calls #####################
###################################################





print(" Welcome to the National Dex\n", "Please input a name or dex number to get started\n")
print(" Type 0 or stop to quit\n")




while switch == True:

  ent = input(" Pokemon Name/Number: ")

  if ent == 0 or str(ent).lower() == "stop": 
    exit()

  try:
      no = int(ent)
      flag = True #int input
  except ValueError:
      flag = False #string input



  if flag == True and int(ent) <= len(dex):
    print("\n")
    checkEntry(dex[int(ent)-1]) 
    display(int(ent))
    #since the array starts at 0, it checks whatever       the input is -1
    
  
    
    

  
  if flag == False:
    print("\n")
    for i in range(len(dex)):
      if (" " + ent).lower() == dex[i].name.lower():
        checkEntry(dex[i])
        display(i+1)
    #since input is string otherwise, check if name matches    


