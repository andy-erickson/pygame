
import pygame
import random

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        changed = False
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            current = arr[j]
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                changed = True
            draw(arr, j+1)

        if changed == False: break
        
def insertionSort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        draw(arr,i)
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = cursor
        draw(arr,pos)


def selectionSort(height):
    speed = int((250 - len(height))/2)
    for i in range(len(height)):
    
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(height)):
            draw(height,j)
            if height[min_idx] > height[j]:
                min_idx = j
    
        # Swap the found minimum element with 
        # the first element 
        draw(height,i,min_idx)
        pygame.time.delay(speed)
        height[i], height[min_idx] = height[min_idx], height[i]
        draw(height,min_idx,i)
        pygame.time.delay(speed)



def fillList(length=15):
    height = []
    for i in range(length):
        height.append(random.randint(3,35))
    return height
    
def draw(height,moving=-1,swap=-1,speed=50):
    pygame.event.pump()
    speed = 250 - len(height)
    if speed < 10:
        speed = 10
    global bubbleButton, insertionButton, selectionButton, moreButton, lessButton
    win.fill((50,50,50))
    pygame.draw.rect(win, (40,40,40), (0, 0, 550 , 100))
    pygame.draw.rect(win, (100,100,100), (0, 0, 550 , 100),2)
    pygame.draw.rect(win, (100,100,100), (400, 0, 200 , 100),2)
    for ele in range(len(height)):
        pygame.draw.rect(win, (100, 150, 100), (50+450/len(height)*ele, 500-(height[ele]*10), 325/len(height) , height[ele]*10 ))
        if ele == moving:
            pygame.draw.rect(win, (200, 150, 100), (50+450/len(height)*ele, 500-(height[ele]*10), 325/len(height) , height[ele]*10 ))
        if ele == swap:
            pygame.draw.rect(win, (150, 75, 75), (50+450/len(height)*ele, 500-(height[ele]*10), 325/len(height) , height[ele]*10 ))
    if moving == -1:
        buttonFont = pygame.font.SysFont("times", 20)
        smallerFont = pygame.font.SysFont("times", 14)
        # bubble sort button
        win.blit(buttonFont.render(('Sorting Algorithm:'), 1, (225,225,225)), (130, 10))
        pygame.draw.rect(win, (150,40,40), (30, 40, 105 , 50))
        bubbleButton = pygame.draw.rect(win, (150,150,150), (30, 40, 105 , 50),1)
        win.blit(buttonFont.render(('Bubble'), 1, (200,200,200)), (50, 52))
        # insertion sort
        pygame.draw.rect(win, (150,40,40), (155, 40, 105 , 50))
        insertionButton = pygame.draw.rect(win, (150,150,150), (155, 40, 105 , 50),1)
        win.blit(buttonFont.render(('Insertion'), 1, (200,200,200)), (170, 52))
        # selection sort
        pygame.draw.rect(win, (150,40,40), (280, 40, 105 , 50))
        selectionButton = pygame.draw.rect(win, (150,150,150), (280, 40, 105 , 50),1)
        win.blit(buttonFont.render(('Selection'), 1, (200,200,200)), (295, 52))        
        # increase list button
        win.blit(smallerFont.render(('Number of Elements'), 1, (225,225,225)), (415, 42)) 
        pygame.draw.rect(win, (75,75,75), (440, 10, 75 , 25))
        moreButton = pygame.draw.rect(win, (150,150,150), (440, 10, 75 , 25),1)
        win.blit(buttonFont.render(('More'), 1, (200,200,200)), (455, 12))
        # decrease list button
        pygame.draw.rect(win, (75,75,75), (440, 65, 75 , 25))
        lessButton = pygame.draw.rect(win, (150,150,150), (440, 65, 75 , 25),1)
        win.blit(buttonFont.render(('Less'), 1, (200,200,200)), (455, 67))        
    pygame.display.update()
    pygame.time.delay(speed)    
            


pygame.init()
win = pygame.display.set_mode((550,550))
pygame.display.set_caption('Sorting GUI')
buttonFont = pygame.font.SysFont("times", 20)

height = fillList(20)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                    
                if bubbleButton.collidepoint(pos):
                    bubbleSort(height)
                    
                if insertionButton.collidepoint(pos):
                    insertionSort(height)
                
                if selectionButton.collidepoint(pos):
                    selectionSort(height)
                    print('click')
                    
                if moreButton.collidepoint(pos):
                    height = fillList(len(height)+10)
                    
                if lessButton.collidepoint(pos):
                    height = fillList(len(height)-10)            
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                    draw(height)   
    draw(height)      
    pygame.display.update()
    pygame.time.delay(10) 
pygame.quit()
    