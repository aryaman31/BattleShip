import random
board = [[[" " for i in range(7)] for j in range(7)] for k in range(2)]
boardH = [[[" " for i in range(7)] for j in range(7)] for k in range(2)]
def intro():
  print("Welcome to TANKS !!")
  print("How To Play : ")
  print("   Place tanks in random locations, then attempt to guess the")
  print("   location of your opponents tanks chance by chance. The aim")
  print("   of the game is guess all of your oppoents tanks")
  print("Best Of Luck !")
  print("=============================================================")
  print("A      2 players")
  print("B      vs Computer")
  print("Q      Quit")
  usin = str(input()).lower()
  op = ["a","b","q"]
  while usin not in op:
    usin = str(input("Invalid Input \n")).lower()
  return usin

def displayBoard(board):
  for i in board:
    k = ""
    for j in i:
      k = k + "[" + j + "]"
    print(k)

def locationValidation(loc,check):
  temp = False
  options = ["1","2","3","4","5","6","7"]
  while temp != True:
    temp = False
    if len(loc) == 3:
      if loc[1] == ",":
        if loc[0] in options and loc[2] in options:
          temp2 = [int(loc[0])-1,int(loc[2])-1]
          if temp2 not in check:
            check.append(temp2)
            temp = True
    if temp != True:
      print("Invalid Input")
      loc = str(input("Enter the Location : "))
  return temp2

def placeTanks(board):
  print("Your Location must be in the format : Row,Coloumn")
  locations = []
  for i in range(0,4):
    loc = str(input("Enter the Location : "))
    loc = locationValidation(loc,locations)
  for i,j in locations:
    board[i][j] = "T"
  return locations
  
def playerPlay(boardH,player,hit,locate,a):
  print("Hit Board : ")
  displayBoard(boardH[player-1])
  loc = str(input("Enter the location to bomb : "))
  loc = locationValidation(loc,hit[player-1])
  boardH[player-1][loc[0]][loc[1]] = "A"
  if loc in locate[a[player-1]]:
    print("Tank Hit !")
    locate[a[player-1]].remove(loc)
    boardH[player-1][loc[0]][loc[1]] = "H"
  else :
    print("Miss")
  return boardH,hit,locate

def main(boardH):
  usin = ""
  while usin != "q":
    usin = intro()

    if usin == "a":
      locate = []    # This will be a 3D array [player][location][x/y]
      for i in range(1,3):
        print("Player",i)
        locate.append(placeTanks(board[i-1]))
        displayBoard(board[i-1])
      print()
      temp = False
      c = 1
      hit = [[],[]]
      a = [1,0]
      while temp != True:
        c += 1
        player = (c%2)+1
        print("Player",player,"turn")
        boardH,hit,locate = playerPlay(boardH,player,hit,locate,a)
        if locate[a[player-1]] == []:
          print("Player",player,"is the winner !")
          temp = True
        print()
        
    elif usin == "b":
      locate = []
      locate.append(placeTanks(board[0]))
      displayBoard(board[0])
      temp = []
      for i in range(0,4):
        cloc = [random.randint(0,6),random.randint(0,6)]
        while cloc in temp:
          cloc = [random.randint(0,6),random.randint(0,6)]
        temp.append(cloc)
      print(temp) # Delete Later
      locate.append(temp)
      print()
      temp = False
      c = 1
      hit = [[],[]]
      a = [1,0]
      while temp != True:
        c += 1
        player = (c%2)+1
        if player == 1:  # User
          boardH,hit,locate = playerPlay(boardH,player,hit,locate,a)
        elif player == 2:
          loc = [random.randint(1,7),random.randint(1,7)]
          while loc in hit[1]:
            loc = [random.randint(1,7),random.randint(1,7)]
          hit[1].append(loc)
          if loc in locate[a[player-1]]:
            locate[a[player-1]].remove(loc)
        if locate[a[player-1]] == []:
          if player == 2:
            print("Computer is the winner !")
          else:
            print("Player 1 is the winner !")
          temp = True
      print()
main(boardH) 
