from PIL import Image
from replit import audio


###################################################
###################Ideas###########################
###################################################

#Implement Type Calculator

#For Resistance function, copy Weakness function code and change prints

#Evolutionary tree/chain + what level/method they evolve by



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

        case "Electric": #Electric/Normal
          print(" Fighting\n", "Ground\n")

        case "Psychic": #Psychic/Normal
          print(" Dark\n", "Bug\n")

        case "Dark": #Dark/Normal
          print(" Fighting\n", "Bug\n")

        case "Steel": #Steel/Normal
          print(" Fighting\n", "Ground\n", "Fire\n")

        case "Fighting": #Fighting/Normal
          print(" Fighting\n", "Flying\n", "Psychic\n")

        case " Ground": #Ground/Normal
          print(" Fighting\n", "Grass\n", "Water\n", "Ice\n")

        case "Rock": #Rock/Normal
          print("Fighting\n", "Grass\n", "Water\n", "Steel\n", "Ground\n")

        case "Poison": #Poison/Normal
          print(" Psychic\n", "Ground\n")

        case "Flying": #Flying/Normal
          print(" Electric\n", "Rock\n", "Ice\n")

        case "Ice": #Ice/Normal
          print(" Fighting\n", "Fire\n", "Rock\n", "Steel\n")

        case "Dragon": #Dragon/Normal
          print(" Fighting\n", "Dragon\n")

        case "Ghost": #Ghost/Normal
          print(" Dark\n")

        case "Bug": #Bug/Normal
          print(" Fire\n", "Flying\n", "Rock\n")
                

        

   ##################  

     case "Fire": #Dual type is Fire

       match type1:

          case "Normal": #Normal/Fire

            print(" Water\n", "Fighting\n", "Ground\n", "Rock\n")

          case "Water": #Water/Fire

            print(" Electric\n", "Ground\n", "Rock\n")

          case "Grass": #Grass/Fire

            print(" Flying\n", "Poison\n")

          case "Electric": #Electric/Fire

            print(" Water\n", "Ground\n", "Rock\n")

          case "Psychic": #Psychic/Fire

            print(" Water\n", "Dark\n", "Ground\n", "Rock\n", "Ghost\n")

          case "Dark": #Dark/Fire

            print(" Water\n", "Fighting\n", "Ground\n", "Rock\n")

          case "Steel": #Steel/Fire

            print(" Water\n", "Fighting\n", "Ground\n")

          case "Fighting": #Fighting/Fire
            print("Water\n", "Flying\n", "Psychic\n", "Ground\n")

          case "Ground": #Ground/Fire
            print(" Water\n", "Ground\n")

          case "Rock": #Rock/Normal
            print(" Water\n", "Ground\n", "Rock\n", "Fighting\n")

          case "Poison": #Poison/Fire
            print(" Water\n", "Ground\n", "Psychic\n", "Rock\n")

          case "Flying": #Flying/Fire
            print(" Water\n", "Rock\n", "Electric\n")

          case "Ice": #Ice/Fire
            print(" Water\n", "Rock\n", "Ground\n", "Fighting\n")

          case "Dragon": #Dragon/Fire
            print(" Rock\n", "Ground\n", "Dragon\n")

          case "Ghost": #Ghost/Fire
            print(" Water\n", "Ground\n", "Rock\n", "Ghost\n", "Dark\n")

          case "Bug": #Bug/Fire
            print(" Water\n", "Rock\n", "Flying\n")

        ##################  

     case "Water": #Dual type is Water

       match type1:

          case "Normal": #Normal/Water

            print(" Electric\n", "Grass\n", "Fighting\n")

          case "Fire": #Fire/Water

            print(" Electric\n", "Ground\n", "Rock\n")

          case "Grass": #Grass/Water

            print(" Flying\n", "Poison\n", "Bug\n")

          case "Electric": #Electric/Water

            print(" Grass\n", "Ground\n")

          case "Psychic": #Psychic/Water

            print(" Electric\n", "Grass\n", "Dark\n", "Ghost\n")

          case "Dark": #Dark/Water

            print(" Electirc\n", "Grass\n","Fighting\n", "Bug\n")

          case "Steel": #Steel/Water

            print(" Electric\n","Fighting\n", "Ground\n")

          case "Fighting": #Fighting/Water
            print(" Electric\n", "Grass\n", "Flying\n", "Psychic\n")

          case "Ground": #Ground/Water
            print(" Grass\n")

          case "Rock": #Rock/Water
            print(" Electric\n", "Grass\n", "Ground\n", "Fighting\n")

          case "Poison": #Poison/Water
            print(" Electirc\n", "Ground\n", "Psychic\n")

          case "Flying": #Flying/Water
            print(" Electric\n", "Rock\n")

          case "Ice": #Ice/Water
            print(" Electric\n", "Grass\n", "Rock\n", "Fighting\n")

          case "Dragon": #Dragon/Water
            print(" Dragon\n")

          case "Ghost": #Ghost/Water
            print(" Electric", "Grass\n", "Ghost\n", "Dark\n")

          case "Bug": #Bug/Water
            print(" Electric\n", "Rock\n", "Flying\n")
          
          ##################  

     case "Grass": #Dual type is Grass

       match type1:

          case "Normal": #Normal/Grass

            print(" Fire\n", "Bug\n", "Poison\n", "Ice\n", "Flying", "Fighting\n")

          case "Fire": #Fire/Grass

            print(" Flying\n", "Poison\n", "Rock\n")

          case "Water": #Water/Grass

            print(" Flying\n", "Poison\n", "Bug\n")

          case "Electric": #Electric/Grass

            print(" Fire\n", "Poison\n", "Bug\n", "Ice\n")

          case "Psychic": #Psychic/Grass

            print(" Fire", "Poison", "Bug\n", "Ice\n", "Flying\n", "Dark\n", "Ghost\n")
            
          case "Dark": #Dark/Grass

            print(" Fire\n", "Poison\n", "Bug\n", "Ice", "Flying", "Fighting\n")
            
          case "Steel": #Steel/Grass

            print(" Fire\n","Fighting\n")

          case "Fighting": #Fighting/Grass
            print(" Fire\n", "Poison\n", "Flying\n", "Ice\n", "Psychic\n")

          case "Ground": #Ground/Grass
            print(" Fire\n", "Flying\n", "Ice\n", "Bug\n")

          case "Rock": #Rock/Grass
            print(" Fighting\n", "Bug\n", "Steel\n")

          case "Poison": #Poison/Grass
            print(" Fire\n","Flying\n", "Ice\n", "Psychic\n")

          case "Flying": #Flying/Grass
            print(" Fire\n", "Poison\n", "Flying\n", "Ice\n", "Rock\n")

          case "Ice": #Ice/Grass
            print(" Fire\n", "Poison\n", "Flying\n", "Bug\n", "Rock\n", "Fighting\n", "Steel\n")

          case "Dragon": #Dragon/Grass
            print(" Poison\n", "Bug\n", "Flying\n", "Ice\n", "Dragon")

          case "Ghost": #Ghost/Grass
            print(" Fire\n", "Flying\n", "Ice\n", "Ghost\n", "Dark\n")

          case "Bug": #Bug/Grass
            print(" Fire\n", "Bug\n", "Ice\n", "Rock\n", "Flying\n")  

          ##################  

     case "Electric": #Dual type is Electric

       match type1:

          case "Normal": #Normal/Electric

            print(" Ground\n", "Fighting\n")

          case "Fire": #Fire/Electric

            print(" Ground\n", "Water\n", "Rock\n")

          case "Water": #Water/Electric

            print(" Ground", "Grass\n")

          case "Grass": #Grass/Electric

            print(" Fire\n", "Poison\n", "Bug\n", "Ice\n")

          case "Psychic": #Psychic/Electric

            print(" Ground\n" , "Dark\n", "Ghost\n")
            
          case "Dark": #Dark/Electric

            print(" Ground\n", "Bug\n", "Fighting\n")
            
          case "Steel": #Steel/Electric

            print(" Ground\n",  "Fire\n", "Fighting\n")

          case "Fighting": #Fighting/Electric
            print(" Ground\n", "Psychic\n")

          case "Ground": #Ground/Electric
            print(" Ground\n", "Water\n", "Grass\n", "Ice\n")

          case "Rock": #Rock/Electric
            print(" Ground\n", "Fighting", "Water\n", "Grass\n")

          case "Poison": #Poison/Electric
            print(" Ground\n", "Psychic\n")

          case "Flying": #Flying/Electric
            print(" Ice\n", "Rock\n")

          case "Ice": #Ice/Electric
            print(" Ground\n", "Fire\n", "Rock\n", "Fighting\n")

          case "Dragon": #Dragon/Electric
            print(" Ground\n", "Ice\n", "Dragon")

          case "Ghost": #Ghost/Electric
            print(" Ground\n", "Ghost\n", "Dark\n")

          case "Bug": #Bug/Electric
            print(" Fire\n", "Rock\n")  

          ##################  

     case "Psychic": #Dual type is Psychic

       match type1:

          case "Normal": #Normal/Psychic

            print(" Dark\n", "Bug\n")

          case "Fire": #Fire/Psychic

            print(" Dark", "Ghost", "Ground\n", "Water\n", "Rock\n")

          case "Water": #Water/Psychic

            print(" Dark\n", "Ghost\n", "Grass\n", "Electric\n", "Bug\n")

          case "Grass": #Grass/Psychic

            print(" Dark\n", "Ghost\n", "Fire\n", "Poison\n", "Bug\n", "Ice\n", "Flying\n")

          case "Psychic": #Electric/Psychic

            print(" Dark\n" , "Ground\n", "Ghost\n", "Bug\n")
            
          case "Dark": #Dark/Psychic

            print(" Bug\n")
            
          case "Steel": #Steel/Psychic

            print(" Ground\n",  "Fire\n")

          case "Fighting": #Fighting/Psychic
            print(" Ghost\n", "Flying\n")

          case "Ground": #Ground/Psychic
            print(" Dark\n", "Ghost\n", "Water\n", "Grass\n", "Ice\n", "Bug\n")

          case "Rock": #Rock/Psychic
            print(" Dark\n", "Ghost\n", "Water\n", "Grass\n", "Ground\n", "Steel\n")

          case "Poison": #Poison/Psychic
            print(" Dark\n", "Ghost\n", "Ground\n")

          case "Flying": #Flying/Psychic
            print(" Dark/n", "Ghost\n", "Ice\n", "Rock\n", "Electric")

          case "Ice": #Ice/Psychic
            print(" Dark\n", "Ghost\n", "Fire\n", "Rock\n", "Steel\n", "Bug\n")

          case "Dragon": #Dragon/Psychic
            print(" Dark", "Ghost\n", "Bug\n", "Ice\n", "Dragon\n")

          case "Ghost": #Ghost/Psychic
            print(" Dark\n", "Ghost\n")

          case "Bug": #Bug/Psychic
            print(" Dark/n", "Ghost","Bug\n", "Fire\n", "Rock\n", "Flying\n")  


#Checklist for types

#___/Normal type:
                
#Normal - N/A
#Fire - Y
#Water - Y
#Grass - Y
#Electric - Y
#Psychic - Y
#Dark - Y
#Steel - Y
#Fighting - Y
#Ground - Y
#Rock - Y
#Poison - Y
#Flying - Y
#Ice - Y
#Dragon - Y
#Ghost - Y
#Bug - Y




      
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

natDex = [" None", " Bulbasaur", " Ivysaur", " Venusaur", " Charmander", " Charmeleon", " Charizard", " Squirtle", " Wartortle", " Blastoise", " Caterpie", " Metapod", " Butterfree", " Weedle", " Kakuna", " Beedrill", " Pidgey"]


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

kakuna = Pokemon(types[12], types [13], natDex[14], 45, 25, 50, 25, 25, 35)

beedrill = Pokemon(types[12], types[13], natDex[15], 65, 90, 40, 45, 80, 75)

pidgey = Pokemon(types[1], types[10], natDex[16], 40, 45, 40, 35, 35, 56)



###################################################
########### Add Each Pokemon To Dex ###############
###################################################


dex = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, caterpie, metapod, butterfree, weedle, kakuna, beedrill, pidgey]




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