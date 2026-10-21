import random
from pathlib import Path
import pygame

_cache = {}
BASE_DIR = Path(__file__).parent
ASTEROID_DIR = BASE_DIR / "assets" / "asteroids"

# Scan the folder once at import time
ASTEROID_PATHS = sorted(
    p for p in ASTEROID_DIR.iterdir()
    if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
)

def load_image(path, size):
    """Load an image, scale it to (w, h), and cache it."""
    key = (str(path), size)
    if key not in _cache:
        img = pygame.image.load(str(path)).convert_alpha()
        _cache[key] = pygame.transform.smoothscale(img, size)
    return _cache[key]

def random_asteroid_path():
    return random.choice(ASTEROID_PATHS)