  DASS Assignment 1

  Instructions to play-
    Run game - run 'python3 main.py' from the repo
    Controls -
      Q/q - Quit
      A/a - Move Left
      D/d - Move Right
      W/w - Move Up
      E/e - Shield Activation ( no shield available in boss level )
      Space - Shoot Bullets (Can only shoot once in 4 seconds in normal mode/ once every 0.3 seconds in boss level)
    Increase your score above 2000 to reach boss level
    Speed Boost is collectible powerup which speeds up all aspects of game
    Magnet appears randomly and attracts the Hero along x-axis

  Files and associated classes-
    main.py - Main logic control of the game
    dragon.py - Contains dragon class and bulletd class (Bullets fired by dragon)
    grid.py - Contains the array of character and color info to be printed
    mandalorian.py - Contains class for Hero
    stats.py - Contains class which contains all stats of current game ( score, time left etc)
    Coins.py - Contains class defining coins present all over the first level of game
    extraFunctions - Contains cmove function
    magnet.py - Contains class for magnet which appears randomly
    objects.py - Contains a superclass which gets inherited by all other objects.   
      Contains functions like checking Overlap, moveLeft, MoveRight etc. which are used by multiple classes.
    config.py - Contains information like framerate, frame height, frame length etc.
    getch.py - defines function to take single character input
    obstacles.py - defined all 4 different obstacle classes and associated attributes
    speed.py - contains class container for speed boost

  OOPS concepts examples-
    Inheritance : Most of the classes inherit from objects class
    Encapsulation : Using classes for all objects and the grid
    Abstraction : Function like Overlap (which check if two objects overlap), Move  
      functions, Getters, Setters etc
    Polymorphism : MoveRight and MoveLeft functions are changed ( from generic
      MoveLeft and MoveRigth in parent objects class) for the Mandalorian class
