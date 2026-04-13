# SpaceInvaders-Arduino-

SpaceInvaders-Arduino- is a Space Invaders arcade game implementation in Python using Pygame. Despite the "Arduino" in the name, this is a desktop game application, not an embedded project.

Main Goal
Create a fully functional Space Invaders-style game with enemies, player shooting, collision detection, enemy fire, meteorites, explosions, and a scoring system with persistent high scores.

Main Data Structures
The codebase uses Pygame Sprites as the primary data structure. Here's how game entities are organized:

Data Structure	Purpose
py.sprite.Group()	Groups to manage collections of sprites for efficient updates and collision detection
playerG	Player ship sprite group
invaders	Group of 30 enemy invaders (3 rows × 10 columns grid)
bullets	Group of player bullets
invadersBullets	Group of enemy fire
meteoriteG	Group of falling meteors
explosionsG	Group of explosion effects
allSprites	Master group for efficient batch updates
score_dict	Dictionary storing top 5 high scores (JSON-persisted)
sounds	Dictionary containing game audio effects
Key Algorithms & Logic
1. Enemy Movement Pattern (invaders.py)
Invaders move in a grid formation with programmed bounce behavior
Three speed tiers (moveTime: 600, 700, 800ms) determine acceleration
Algorithm tracks:
moveNumber: current position in movement cycle
rightMoves / leftMoves: distance boundaries for direction changes
direction: +1 (right) or -1 (left)
Adjusts movement speed as enemies are eliminated
2. Collision Detection System (SpaceInvaders.py - check_collisions())
Uses pygame.sprite.groupcollide() to detect 5 collision types:

Player bullets ↔ Enemy bullets
Player bullets ↔ Meteorites
Player bullets ↔ Invaders
Enemy bullets ↔ Player ship
Invaders ↔ Player ship
Meteorites ↔ Player ship
3. Enemy Shoot Algorithm (make_enemies_shoot())
Randomly selects one column from active invaders
Finds the bottommost invader in that column (last one)
Only that invader shoots every 700ms
Creates realistic column-based fire pattern
4. Difficulty Scaling (update_enemy_speed())
Increases meteor spawn rate and speed based on score:
Score > 1000: faster meteors
Score > 2000: even faster
Score > 3000: maximum difficulty
Game accelerates as player progresses
5. Persistence System
highscores.json: Stores top 5 scores
JSON loading/dumping methods handle persistent storage
Scores auto-loaded on game restart
6. Game State Machine
Three main states:

mainScreen: Welcome screen with high scores
startGame: Active gameplay
gameOver: Game over screen with 5-second delay before reset
Game Flow
Code
1. Welcome Screen (display high scores)
   ↓ (any key press)
2. Initialize Game (create player, enemies, sprites)
   ↓
3. Game Loop (per frame at 60 FPS):
   - Handle input (arrow keys to move, space to shoot)
   - Update all sprites
   - Check collisions
   - Manage enemy fire
   - Spawn meteorites
   - Render score
   ↓ (all enemies killed)
4. Level Complete (3-second delay, reinitialize)
   ↓ (lives = 0)
5. Game Over → Save score → Return to welcome screen
Key Features
✅ Sprite-based rendering using Pygame
✅ Configurable FPS (60 FPS target)
✅ Sound effects for shooting, explosions, and impacts
✅ Progressive difficulty scaling
✅ Persistent high score tracking
✅ Collision detection with multiple entity types
✅ Visual explosion effects with animation timing
✅ Player lives system (1 life)
✅ Dynamic player weapon upgrade (dual bullets after 310 points)
