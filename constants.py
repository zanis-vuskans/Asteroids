SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#Player constants
PLAYER_RADIUS = 30 # the radius of the player's ship
PLAYER_LINE_WIDTH = 2 # the width of the lines that draw the player's ship
PLAYER_COLOR = (255, 255, 255) # the color of the player's ship
PLAYER_TURN_SPEED = 300 # represent the player's turn speed
PLAYER_SPEED = 200 # represent the player's speed
PLAYER_LIVES = 3
PLAYER_RESPAWN_INVULNERABLE_SECONDS = 2


SHOT_RADIUS = 5 # the radius of the player's shots
SHOT_COLOR = (255, 255, 0) # the color of the player's shots
SHOT_LINE_WIDTH = 1 # the width of the lines that draw the shots
PLAYER_SHOOT_SPEED = 500 # the speed at which the player shoots
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3 # the cooldown time between shots
SHOT_LINE_LENGTH = 12  # visual length only, doesn't affect collisions

#asteroid constants
ASTEROID_COLOR = (255, 0, 0) # the color of the asteroid
ASTEROID_LINE_WIDTH = 2 # the width of the lines that draw the asteroid
ASTEROID_MIN_RADIUS = 20 
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS