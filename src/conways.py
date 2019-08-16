import pygame
import random

# Define some colors and other constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500
CELL_SIZE = 20
# 1. set up initial states

cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1
# next_states = []

generation = 0
is_paused = False


for i in range(len(cur_states)):
    cur_states[i] = random.randint(0, 1)


pygame.init()

# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption(f"Conway's Game of Life, Generation: {generation}")

# Buttons
pause_button = pygame.draw.rect(screen, BLUE, pygame.Rect(200, 420, 100, 50))


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

    # --- Game logic should go here
    generation += 1
    neighbors = 0
    pygame.display.set_caption(
        f"Conway's Game of Life, Generation: {generation}")
    if event.type == pygame.MOUSEBUTTONDOWN:
        click_pos = pygame.mouse.get_pos()
        if pause_button.collidepoint(click_pos):
            is_paused = not is_paused
    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    # 3. night 2: work on rules that i) look at all neighbors, ii) save new state in
    if not is_paused:
        next_states = [0] * 400
        for item in cur_states:
            if cur_states[item] >= 2:
                next_states += 1
            if cur_states[item] == 3:
                next_states += 1
            if cur_states[item] > 3:
                next_state += 0

        next_states[item] = cur_states
            
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)

    # --- Drawing code should go here
    # pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))
    cur_index = 0
    x = 5
    while x < WIN_SIZE:
        y = 5
        while y < WIN_SIZE:
            # 2. draw rectangles based on states
            state = cur_states[cur_index]
            if state == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20))
            # 4. draw based on values in next_state
            cur_index += 1
            y += 25
        x += 25
    #  buttons locations
    pause_button = pygame.draw.rect(
        screen, BLUE, pygame.Rect(200, 420, 100, 50))
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render('Play/Pause', True, (25, 28, 54))
    screen.blit(text, pause_button)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(5)

# Close the window and quit.
pygame.quit()
