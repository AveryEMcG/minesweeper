"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random

board = []
displayBoard = []
bombs = []

def getWinConditions():
    for i in range(10):
        for j in range(10):
            if displayBoard[i][j] == ' ':
                return False
            if (displayBoard[i][j] == "!") and ((i,j) not in bombs):
                return False
    return True

def incrementBombCount(i,j):
    
    cells = []
    cells.append([i-1,j-1])
    cells.append([i-1,j])
    cells.append([i-1,j+1])
    
    cells.append([i,j-1])
    cells.append([i,j+1])


    cells.append([i+1,j-1])
    cells.append([i+1,j])
    cells.append([i+1,j+1])

    for c in cells:
        x,y = c
        if not (x<0 or x>9 or y<0 or y>9):
            if board[x][y] != 'X':
                board[x][y] =str(int(board[x][y])+ 1)

def setupBoard():
    for i in range (10):
        board.append([])
        displayBoard.append([])
        for j in range (10):
            board[i].append([])
            displayBoard[i].append([])
            randomNum = random.randint(0,10)
            if randomNum == 1:
                board[i][j]='X'
                bombs.append((i,j))
            else:
                board[i][j]='0'
            displayBoard[i][j]=' '
    i = 0
    j = 0
    for row in board:
        for cell in row:
            if cell == 'X':
                incrementBombCount(i,j)
            j+=1
        i+=1
        j = 0


def processClickedSquare(x,y,(leftClick,middleClick,rightClick)):
    if (0<=x<=9) and (0<=y<=9):
        if leftClick:
            displayBoard[y][x] = board[y][x]
            if displayBoard[y][x] == "X":
                return False
        if rightClick:
            displayBoard[y][x] = "!"
        return True


def main():

    
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Arial', 30)


    setupBoard()
    gameOver = False
    win = False
    
    # Set the width and height of the screen [width, height]
    size = (300, 300)
    screen = pygame.display.set_mode(size)
        
    pygame.display.set_caption("Avery's Minesweeper")
    
    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if gameOver or win:
                    setupBoard()
                    gameOver = False
                    win = False
                else:
                    mouseX,mouseY = event.pos
                    mouseX/=30
                    mouseY/=30
                    if not (processClickedSquare(mouseX,mouseY, pygame.mouse.get_pressed())):
                        gameOver = True
                    elif getWinConditions():
                        win = True
        # --- Game logic should go here
    
        # --- Screen-clearing code goes here
    
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
    
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(WHITE)
        

        for i in range(10):
            for j in range(10):
                textsurface = myfont.render(displayBoard[i][j], False, (0,0,0))
                screen.blit(textsurface,((j*30)+5,i*30))
                l,t,w,h = textsurface.get_rect()
                l = j*30
                t = i*30
                w = 30
                h = 30
                pygame.draw.rect(screen, (0,0,0), (l,t,w,h), 2)

        if gameOver:
                textsurface = myfont.render("YOU LOST!", False, (255,0,0))
                screen.blit(textsurface,(0,0))
        elif win:
                textsurface = myfont.render("YOU WON!", False, (0,255,0))
                screen.blit(textsurface,(0,0))
        # --- Drawing code should go here
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
        # --- Limit to 60 frames per second
        clock.tick(60)
    
    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    main()