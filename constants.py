SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#Player constants
PLAYER_RADIUS = 20 # the radius of the player's ship
PLAYER_LINE_WIDTH = 2 # the width of the lines that draw the player's ship
PLAYER_COLOR = (255, 255, 255) # the color of the player's ship
PLAYER_TURN_SPEED = 300 # represent the player's turn speed
PLAYER_SPEED = 200 # represent the player's speed

#asteroid constants
ASTEROID_COLOR = (255, 0, 0) # the color of the asteroid
ASTEROID_LINE_WIDTH = 2 # the width of the lines that draw the asteroid
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS