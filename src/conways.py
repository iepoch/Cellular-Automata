import pygame
import random

# Define some colors and other constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500

# 1. Create a set of initial states with simple pattern (Ex. blinker)
cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1
# next_states = None * 400

generation = 0
is_paused = False
# Current States
# cur_states = [0] * 400
# for i in range(len(cur_states)):
#     cur_states[i] = random.randint(0, 1)
CELL_SIZE = 20
num_cols = int(WIN_SIZE / CELL_SIZE)
num_rows = int(WIN_SIZE / CELL_SIZE)
print(f'Columns: {num_cols} \nRows: {num_rows}')
grids = [
    [[0] * num_rows] * num_cols,
    [[0] * num_rows] * num_cols
]
active_grid = 0
# Allow users to choose between serveral predefined intial states

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption(f"Conway's Game of Life {generation}")

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
    pygame.display.set_caption(f"Conway's Game of Life {generation}")

# Pause/Play
if event.type == pygame.MOUSEBUTTONDOWN:
    click_pos = pygame.mouse.get_pos()
    if pause_button.pygame.Rect.collidepoint(click_pos):
        is_paused = not is_paused

# Main SIMULATION Logic
new_states = [0] * 400

if not is_paused in range(len(cur_states)):
    for index in range(len(cur_states)):

        # Calc number of live neighbors
        e = index + CELL_SIZE
        w = index - CELL_SIZE
        n = index - 1
        s = index + 1
        ne = n + 1
        nw = n - 1
        se = s + 1
        sw = s - 1
        live_neighbors = 0
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.    live_neighbors = 0
        if e < len(cur_states) and cur_states[e] == 1:
            live_neighbors += 1
        if w > 0 and cur_states[w] == 1:
            live_neighbors += 1
        if n % CELL_SIZE != CELL_SIZE - 1 and cur_states[n] == 1:
            live_neighbors += 1
        if s % CELL_SIZE != CELL_SIZE - 1 and cur_states[s] == 1:
            live_neighbors += 1
        if ne < len(cur_states) and ne % CELL_SIZE != CELL_SIZE - 1 and cur_states[ne] == 1:
            live_neighbors += 1
        if se < len(cur_states) and se % CELL_SIZE != CELL_SIZE - 1 and cur_states[se] == 1:
            live_neighbors += 1
        if nw > 0 and nw % CELL_SIZE != CELL_SIZE - 1 and cur_states[nw] == 1:
            live_neighbors += 1
        if sw > 0 and sw % CELL_SIZE != CELL_SIZE - 1 and cur_states[sw] == 1:
            live_neighbors += 1
        if cur_states[index] == 1:
            if live_neighbors < 2:
                new_states[index] = 0
            elif live_neighbors > 3:
                new_states[index] = 0

            else:
                new_states[index] = 1

        else:
            if live_neighbors == 3:
                new_states[index] = 1
            else:
                new_states[index] = 0

        cur_states = new_states


#         # Any live cell with two or three live neighbours lives on to the next generation.
#         if live_neighbors < 2:
#             next_states[index] = 0
# # Any live cell with more than three live neighbours dies, as if by overpopulation.

#         elif live_neighbors > 3:
#             next_states[index] = 0
# else:
#         if live_neighbors == 3:
#             next_states[index] = 1
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# 3. Work on rules that i) look at all neighbors, ii) save new state
# in next_states[]

# --- Screen-clearing code goes here

# Here, we clear the screen to gray. Don't put other drawing commands
# above this, or they will be erased with this command.
screen.fill(GRAY)

# --- Drawing code should go here
cur_index = 0
x = 5
while x < 500:
    y = 5
    while y < 500:
            # 2. Draw based on values in cur_states
        state = cur_states[cur_index]
        # 4. Draw based on values in next_states
        if state == 0:
            pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20))
        else:
            pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20))
        cur_index += 1
        y += 25
    x += 25
    # button example
pause_button = pygame.draw.rect(
    screen, BLUE, pygame.Rect(200, 450, 100, 25))
font = pygame.font.Font('freesansbold.ttf', 16)
text = font.render('Play/Pause', True, (14, 28, 54))
screen.blit(text, pause_button)

pygame.display.flip()

# --- Limit to 5 frames per second
clock.tick(5)

# Close the window and quit.
pygame.quit()
