from PIL import Image, ImageDraw
from displayhatmini import DisplayHATMini

from conway import GameOfLife
from terminal import TerminalManager
from renderer import Renderer

# Create terminal manager to set up key handling etc
terminal_manager = TerminalManager()
# Create image buffer to render into
buffer = Image.new("RGB", (DisplayHATMini.WIDTH, DisplayHATMini.HEIGHT), 'black')
# Create renderer to handle image updates
renderer = Renderer(8, ImageDraw.Draw(buffer))
# Create display hat interface and turn the LED off
displayhatmini = DisplayHATMini(buffer)
displayhatmini.set_led(0, 0, 0)
# Create Game of Life simulation with tiles based on screen size and tile size
game = GameOfLife(DisplayHATMini.WIDTH // renderer.tileSize, DisplayHATMini.HEIGHT // renderer.tileSize)

running = True
while running:
    # Clear the display ready for new frame - remove this can give some cool plasma effects
    renderer.clear(DisplayHATMini.WIDTH, DisplayHATMini.HEIGHT)
    if terminal_manager.is_escape_pressed():
        # Exit the loop if user presses escape
        running = False
    else:
        # Update simulation, update renderer, and refresh the display
        game.tick()
        renderer.output(game)
        displayhatmini.display()
    # Currently runs at a healthy frame-rate, if you want to limit it then add a wait here

# Clean up the terminal changes made on launch
terminal_manager.close()
