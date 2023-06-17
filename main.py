
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
  def __init__(self,t1, t2, n, h, s, a, d, sa, sd):

    self.type1 = t1
    self.type2 = t2

    self.name = n
    self.hp = h
    self.spd = s
    self.atk = a
    self.dfs = d
    self.spatk = sa
    self.spdfs = sd


def weakness(type1, type2): #function for weakness

  match type2:

    case "None": #If no dual type

      match type1:

        case "Grass":

          print(" Fire\n", "Ice\n", "Flying\n", "Poison\n", "Bug\n") 
          
        case "Fire":

          print(" Water\n", "Ground\n", "Rock\n")

        case "Water":

          print(" Grass\n", "Electric\n")

        case "Electric":

          print(" Ground\n")

        case "Psychic":

          print(" Dark\n", "Bug\n", "Ghost\n")

  



         
  



bulbasaur = Pokemon("Grass", "None", "Bulbasaur", 0, 0, 0, 0, 0 , 0)

dex = [bulbasaur]

#fi this line 
print(weakness(dex[0].type1, dex[0].type2))
#print(dex[0].name)