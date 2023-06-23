from PIL import Image



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

#types = ["None","Normal", "Fire", "Water", "Grass", "Electric", "Fighting", "Psychic", "Dark", "Steel", "Flying", "Ice", "Bug", "Poison", "Ground", "Rock", "Ghost", "Dragon", "Fairy"]


def checkName(p):

  print(p.name)







###################################################
###################################################




def weakness(type1, type2): #function for weakness


  match type2:

    case "None": #If no dual type

      match type1:

        case "Normal":

          print(" Fighting\n")

        case "Fire":

          print(" Water\n", "Ground\n", "Rock\n")

        case "Grass":

          print(" Fire\n", "Ice\n", "Flying\n", "Poison\n", "Bug\n") 
          
        case "Water":

          print(" Grass\n", "Electric\n")

        case "Electric":

          print(" Ground\n")

        case "Psychic":

          print(" Dark\n", "Bug\n", "Ghost\n")

        case "Dark":

          print(" Fighting\n", "Bug\n")

        case "Steel":

          print(" Fire\n", "Fighting", "Ground")

        case "Fighting":

          print(" Psychic\n", "Flying\n")
          


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
  




  #Also print the total
  # t = 0
  # And t should equal the sum of all the stats
  
  # ADD LINE FOR SUMMING HERE

  # Uncomment the line below by deleting the #
  #print("Total:", t, "\n")

  

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


types = ["None","Normal", "Fire", "Water", "Grass", "Electric", "Fighting", "Psychic", "Dark", "Steel", "Flying", "Ice", "Bug", "Poison", "Ground", "Rock", "Ghost", "Dragon", "Fairy"]

flag = False
switch = True


#Put each pokemon in here, so we can use the array and dex number ~B-)>
natDex = [" None", " Bulbasaur", " Ivysaur", " Venusaur", " Charmander", " Charmeleon", " Charizard", " Squirtle", " Wartortle", " Blastoise"]


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

#  n = 18   Fairy

#--------------------------------------------------#


bulbasaur = Pokemon(types[4], types[0], natDex[1], 45, 49, 49, 65, 65, 45)

ivysaur = Pokemon(types[4], types[13], natDex[2], 60, 62, 63, 80, 80, 60)

venusaur = Pokemon(types[4], types[13], natDex[3], 80, 82, 83, 100, 100, 80)

charmander = Pokemon(types[2], types[0], natDex[4], 39, 52, 43, 60, 50, 65)




###################################################
########### Add Each Pokemon To Dex ###############
###################################################


dex = [bulbasaur, ivysaur, venusaur, charmander]




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
      flag = True
  except ValueError:
      flag = False



  if flag == True and int(ent) <= len(dex):
    print("\n")
    checkEntry(dex[int(ent)-1])

    if int(ent) < 10:
      with Image.open("/Downloads/pkmn", "00" + str(ent) + ".gif") as img:
        img.show()
            
    if int(ent) >= 10 and i < 100:
      with Image.open("0" + str(ent) + ".gif") as img:  
        img.show()
        
    if int(ent) >= 100:
      with Image.open(str(ent) + ".gif") as img:  
        img.show()

  
  if flag == False:
    print("\n")
    for i in range(len(dex)-1):
      if (" " + ent).lower() == dex[i].name.lower():
        checkEntry(dex[i])

        if i < 10:
          with Image.open("00" + str(i)+ ".gif") as img:
            img.show()
            
        if i >= 10 and i < 100:
          with Image.open("0" + str(i) + ".gif") as img:  
            img.show()
        if i >= 100:
          with Image.open(str(i) + ".gif") as img:  
            img.show()