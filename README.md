# Snake
My own version of the snake arcade game, with a couple twists (multiplayer, etc.)
Currently, this game is a work in progress...

  The goal of the game is to create a snake game in which multiple snakes can coexist
  
  Right now, I'm still working on fixing/improving:
    1.The dual controls for the snake(s)
    2.The function in board.py which returns a list of "bad" locations (locations which the apple shouldn't place)
      The function is really redundant...plan on updating soon, still serves its purpose though
    3.Constantly looking for other problems/areas that could be improved

I developed this game to gain a better understanding of object oriented programming. I also wanted to
practice writing "clean" code, so I split my classes into files, and called funnctions in main.py...

Enjoy!
  -Benjamin Hatch, High School Senior @ Granada High School
  
***note-change the "grid = Board(15,15,1) #rows, cols, number of apples" and
"grid.makeSnakes(1,5) #number of snakes, length of snakes at start"
to add snakes or apples and adjust snake length @ the start of the game***
