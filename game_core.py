#!/usr/bin/env python3

# trunc8 did this

import json
import numpy as np
import time

from helper import Helper

class Game:
  def __init__(self):
    # Declaring Member variables
    self.grid = None
    self.UPDATE_RATE = None
    self.NUM_OF_GENERATIONS = None

    # Helper class contains some handy utilities
    self.helper = Helper()


  def startGame(self):
    '''
    This function is the epicenter of action!
    It commands the flow of the program.
    '''
    self.helper.clearConsole()
    self.getInput()
    
    for i in range(self.NUM_OF_GENERATIONS):
      self.helper.clearConsole()
      print(f"Generation {i+1}")
      self.updateGrid()
      self.helper.printGrid(self.grid)
      print("\n\n\nPress <Ctrl+C> to exit early", end='')
      time.sleep(1./self.UPDATE_RATE)


  def getInput(self):
    '''
    User is allowed to choose a pattern to start the game
    '''
    print("Welcome, Player!\n")
    patterns = '''Below is the list of available patterns:
    >> block
    >> beehive
    >> loaf
    >> boat
    >> tub
    >> blinker
    >> toad
    >> beacon
    >> glider
    >> lwss (stands for Light-weight spaceship)
    >> mwss (stands for Middle-weight spaceship)
    >> hwss (stands for Heavy-weight spaceship)
    '''
    print(patterns)
    user_pattern = input("Please type the name of a pattern (Press <Enter> to select the default= Glider): ") or "glider"
    try:
      with open("config.json") as file:
        config = json.load(file)
        self.UPDATE_RATE = config["update_rate"]
        self.NUM_OF_GENERATIONS = config["num_of_generations"]
        self.grid = np.array(config[user_pattern.lower()])
        print("\n\nSuccess! Values loaded from config")
        time.sleep(1)
    except:
      print("\n\nERROR: Either typo in entered pattern name or "+
        "error in config.json. Proceeding with default values!")
      self.UPDATE_RATE = 5            # Hz
      self.NUM_OF_GENERATIONS = 1000
      self.grid = np.array([          # Glider
          [1, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
      ])
      time.sleep(3)
      return


  def updateGrid(self):
    '''
    KERNEL = [[1,1,1],
              [1,0,1],
              [1,1,1]]
    Convolving with this efficiently provides us
    the neighbor count for all cells
    '''
    KERNEL = np.ones((3,3))
    KERNEL[1,1] = 0

    # Wrap around padding: any pattern going outside the
    # grid will wrap around from the other side
    left_col = self.grid[:,[-1]]
    right_col = self.grid[:,[0]]
    grid_copy = np.hstack((left_col, self.grid, right_col))
    top_row = grid_copy[-1,:]
    bottom_row = grid_copy[0,:]  
    grid_copy = np.vstack((top_row, grid_copy, bottom_row))
    neighbour_grid = self.helper.conv2d(grid_copy, KERNEL)

    # Unsustainable neighbors, definitely dead
    dead_mask = np.bitwise_or(neighbour_grid < 2, neighbour_grid > 3)
    self.grid[dead_mask] = 0

    # Resurrecting neighbors, already live cells unaffected
    # Dead cells get revived
    resurrect_mask = neighbour_grid == 3
    self.grid[resurrect_mask] = 1

    return