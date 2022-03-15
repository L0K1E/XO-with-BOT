import os

Board = {
    7 : ' ', 8 : ' ', 9 : ' ',
    4 : ' ', 5 : ' ', 6 : ' ',
    1 : ' ', 2 : ' ', 3 : ' '
}

def Banner():
    print('''
    
                                                      ,----..   
                                     ,--,     ,--,   /   /   \  
                                     |'. \   / .`|  /   .     : 
                                     ; \ `\ /' / ; .   /   ;.  |
                                     `. \  /  / .'.   ;   /  ` ;
                                      \  \/  / ./ ;   |  ; \ ; |
                                       \  \.'  /  |   :  | ; | '
                                        \  ;  ;   .   |  ' ' ' :
                                       / \  \  \  '   ;  \; /  |
                                      ;  /\  \  \  \   \  ',  / 
                                    ./__;  \  ;  \  ;   :    /  
                                    |   : / \  \  ;  \   \ .'   
                                    ;   |/   \  ' |   `---`     
                                    `---'     `--`              
    ''')

def OWins():
    print("""
                         ..|''||      '|| '||'  '|' '||' '|.   '|'  .|'''.|     .|.
                        .|'    ||      '|. '|.  .'   ||   |'|   |   ||..  '     |||
                        ||      ||      ||  ||  |    ||   | '|. |    ''|||.     '|'
                        '|.     ||       ||| |||     ||   |   |||  .     '||     | 
                         ''|...|'         |   |     .||. .|.   '|  |'....|'      . 
                                                                                '|'
    """)

def XWins():
    print("""
                        '||' '|'    '|| '||'  '|' '||' '|.   '|'  .|'''.|     .|.
                          || |       '|. '|.  .'   ||   |'|   |   ||..  '     |||
                           ||         ||  ||  |    ||   | '|. |    ''|||.     '|'
                          | ||         ||| |||     ||   |   |||  .     '||     | 
                        .|   ||.        |   |     .||. .|.   '|  |'....|'      . 
                                                                              '|'
    """)

def DisplayBoard(Board):
    print(f"""
                                    {Board[7]} | {Board[8]} | {Board[9]}
                                    ---------
                                    {Board[4]} | {Board[5]} | {Board[6]}
                                    ---------
                                    {Board[1]} | {Board[2]} | {Board[3]}
    """)
    print('\n\n\n')

def IsEmpty(Position):
    if Board[Position] == ' ':
        return True
    else:
        return False

def CheckDraw():
    for keys in Board.keys():
        if Board[keys] == ' ':
            return False
    
    return True

def CheckWin():
    # Vertical Wins
    if Board[1] == Board[2] and Board[1] == Board[3] and Board[1] != ' ':
        return True
    elif Board[4] == Board[5] and Board[4] == Board[6] and Board[4] != ' ':
        return True
    elif Board[7] == Board[8] and Board[7] == Board[9] and Board[7] != ' ':
        return True
    # Horizontal Wins
    elif Board[7] == Board[4] and Board[7] == Board[1] and Board[7] != ' ':
        return True
    elif Board[8] == Board[5] and Board[8] == Board[2] and Board[8] != ' ':
        return True
    elif Board[9] == Board[6] and Board[9] == Board[3] and Board[9] != ' ':
        return True
    # Diagonal Wins
    elif Board[7] == Board[5] and Board[7] == Board[3] and Board[7] != ' ':
        return True
    elif Board[9] == Board[5] and Board[9] == Board[1] and Board[9] != ' ':
        return True
    else:
        return False

def CheckWhichMarkWon(mark):
    # Vertical Wins
    if Board[1] == Board[2] and Board[1] == Board[3] and Board[1] == mark:
        return True
    elif Board[4] == Board[5] and Board[4] == Board[6] and Board[4] == mark:
        return True
    elif Board[7] == Board[8] and Board[7] == Board[9] and Board[7] == mark:
        return True
    # Horizontal Wins
    elif Board[7] == Board[4] and Board[7] == Board[1] and Board[7] == mark:
        return True
    elif Board[8] == Board[5] and Board[8] == Board[2] and Board[8] == mark:
        return True
    elif Board[9] == Board[6] and Board[9] == Board[3] and Board[9] == mark:
        return True
    # Diagonal Wins
    elif Board[7] == Board[5] and Board[7] == Board[3] and Board[7] == mark:
        return True
    elif Board[9] == Board[5] and Board[9] == Board[1] and Board[9] == mark:
        return True
    else:
        return False

def CheckForWin(Letter):
    if(CheckWin()):
        if Letter == 'X':
            os.system('cls')
            DisplayBoard(Board)
            XWins()
            exit()
        else:
            os.system('cls')
            DisplayBoard(Board)
            OWins()
            exit()

def CheckForDraw():
    if(CheckDraw()):
        os.system('cls')
        DisplayBoard(Board)
        print("                                         Match Draw !")
        exit()

def BoardInput(Position, Letter):
    if IsEmpty(Position):
        Board[Position] = Letter

    else:
        os.system('cls')
        DisplayBoard(Board)
        print("                                 Invalid Move !")
        Position = int(input("                              Enter the Position (Player):"))
        BoardInput(Position, Letter)
        return

def PlayerMove(Player):
    DisplayBoard(Board)
    Position = int(input("                              Enter the Position (Player):"))
    BoardInput(Position, Player)
    return

def BotMove(Bot, Player):
    BestScore = -1000
    BestMove = 0

    for key in Board.keys():
        if(Board[key] == ' '):
            Board[key] = Bot
            Score = minimax(Board, 0, False, Bot, Player)
            Board[key] = ' '
            if(Score > BestScore):
                BestScore = Score
                BestMove = key
    # Position = int(input("Enter the Position (Bot):"))
    BoardInput(BestMove, Bot)
    return

def minimax(Board, Depth, IsMaximizing, Bot, Player):
    if CheckWhichMarkWon(Bot):
        return 100
    elif CheckWhichMarkWon(Player):
        return -100
    elif CheckDraw():
        return 0

    if IsMaximizing:
        BestScore = -1000
        for key in Board.keys():
            if(Board[key] == ' '):
                Board[key] = Bot
                Score = minimax(Board, 0, False, Bot, Player)
                Board[key] = ' '
                if(Score > BestScore):
                    BestScore = Score
        return BestScore
    else:
        BestScore = 800
        for key in Board.keys():
            if(Board[key] == ' '):
                Board[key] = Player
                Score = minimax(Board, 0, True, Bot, Player)
                Board[key] = ' '
                if(Score < BestScore):
                    BestScore = Score
        return BestScore


def GetPlayerChoice():
    choice = int(input("""
                                    Select X or O :
                                     X ) Press 1
                                     O ) Press 2
    """))
    if choice == 1:
        Player = 'X'
        Bot = 'O'
        return Player, Bot

    elif choice == 2:
        Player = 'O'
        Bot = 'X'
        return Player, Bot      
    else:
        print("                                     Invalid Choice")
        GetPlayerChoice()

def Game():
    os.system('cls')
    Banner()
    Player, Bot = GetPlayerChoice()
    os.system('cls')
    while not CheckWin():
        if Player == 'X':
            PlayerMove(Player)
            CheckForWin(Player)
            CheckForDraw()
            os.system('cls')
            BotMove(Bot, Player)
            CheckForWin(Bot)            
            CheckForDraw()
        else:
            BotMove(Bot, Player)
            CheckForWin(Bot)               
            CheckForDraw() 
            os.system('cls')
            PlayerMove(Player)
            CheckForWin(Player)            
            CheckForDraw()
            

Game()