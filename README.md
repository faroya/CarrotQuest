# A simple Pygame project

In this project, I have implemented a simple game using the Pygame library where a rabbit tries to catch falling carrots. Each time a carrot is caught, the score increases. Here are the details of the project.

## Dependencies

- Pygame: Used for game development, managing assets like images and sounds, and handling events.

## File Structure

- `main.py`: The main script which contains the game logic.
- `models.py`: This script should contain the definitions for `Carrot` and `Rabbit` classes (not provided here).
- `art/bg.png`: Background image file.
- `eat.wav`: Sound file which plays when a carrot is caught.

## How to Run

To run the game, simply execute the `main.py` script.

```bash
python main.py
```

## Code Structure

### Importing Necessary Modules

```python
import pygame
from models import *
```

### Initializing Pygame and Variables

We initialize Pygame and necessary variables including the screen dimensions and FPS.

```python
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
Fps = 30
screen_w = 580
screen_h = 620
```

### Loading Assets

Loading necessary assets like background image and eating sound.

```python
bg = pygame.image.load("art/bg.png").convert_alpha()
bg = pygame.transform.scale(bg, (screen_w, screen_h))
eat = pygame.mixer.Sound("eat.wav")
```

### Creating Rabbit and Carrots

Initializing the rabbit and carrots objects. The carrots are created in a list with randomized positions.

```python
rect1, rabbit = Rabbit(300, screen_h - 135)
carrots = []
for carrot in range(4):
    carrots.append(Carrot(random.randint(20, screen_w-20), random.randint(-50, -10)))
```

### Main Game Loop

Within the main game loop, we perform several actions including checking for events, handling collision detection, and updating the positions of carrots and rabbit.

```python
while run:
    # ... (rest of the loop)
```

### Drawing the Scene

Within the main loop, we have a section where we draw the carrots, rabbit, and the score onto the window.

```python
win.blit(rabbit, (rect1.x, rect1.y))
text = font.render(str(score), 1, (255, 255, 255))
win.blit(text, (screen_w/2.1, 20))
pygame.display.update()
win.blit(bg, (0, 0))
```

## Conclusion

This is a simple Pygame project to showcase the creation of a game with basic collision detection and scorekeeping. You can further expand this project by adding more features and refining the existing ones.
