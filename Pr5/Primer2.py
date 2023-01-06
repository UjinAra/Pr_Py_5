#Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
#Игра начинается с хода человека, который ставит крестики
board = list(range(1,10))

def drawBoard(board):
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")

def takeInput(playerXO):
    valid = False
    while not valid:
        playerAns = input("Куда поставим " + playerXO+"? ")
        try:
            playerAns = int(playerAns)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if playerAns >= 1 and playerAns <= 9:
            print (playerAns)
            print (board[playerAns-1])
            print (playerXO)
            if (str(board[playerAns-1]) not in "XO"):
                board[playerAns-1] = playerXO
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def checkWin(board):
    winCoord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in winCoord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        drawBoard(board)
        if counter % 2 == 0:
            takeInput("X")
        else:
            takeInput("O")
        counter += 1
        if counter > 4:
            tmp = checkWin(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    drawBoard(board)

main(board)