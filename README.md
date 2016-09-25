# Game-of-Life

###About
This python program is the simulation of popular game 'Game of Life' by 1970 British Mathematician John Conway<br>
The game mimics the chaotic yet patterned growth of a colony of biological organisms<br>
The "game" takes place on a two-dimensional grid consisting of "living" and "dead" cells, and the rules to step from generation to generation are simple:<br>
+ __Overpopulation:__ if a living cell is surrounded by more than three living cells, it dies.
+ __Stasis:__ if a living cell is surrounded by two or three living cells, it survives.
+ __Underpopulation:__ if a living cell is surrounded by fewer than two living cells, it dies.
+ __Reproduction:__ if a dead cell is surrounded by exactly three cells, it becomes a live cell.
<br>

More on [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)[Wikipedia]

##Usage
To use the program, go to the Game-of-Life directory and in terminal run the game-of-life.py using following command:
`python game-of-life.py`

##Patterns
The program supports popular patterns<br>
To uses them, just change the `pattern ` variable in `game-of-life.py` file to one of the following patterns:<br>
+ random
+ glider
+ glider_gun
+ diehard
+ boat
+ r_pentomino
+ beacon
+ acorn
+ spaceship
+ block_switch_engine
+ pulsar
+ blinker
+ toad
<br>

For example, if you want to use glider pattern, change pattern variable from:<br>
`pattern = patterns.random`
<br>to:<br>
`pattern = patterns.glider`
<br>
