#!/usr/bin/env python3

# trunc8 did this

import numpy as np
import unittest

from game_core import Game

class Test_Game_Solution(unittest.TestCase):

  def test_after_5_runs(self):
    '''
    Verifying that all cells are obeying Conway's
    rules after RUNS number of updates
    '''
    game = Game()
    game.grid = np.array([          # Glider
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ])
    RUNS = 5
    for i in range(RUNS):
      game.updateGrid()
      if i==(RUNS-2):
        prev_grid = game.grid.copy()        
    rows, cols = game.grid.shape
    directions = [[1,0], [1,1], [0,1], [-1,1],
                  [-1,0], [-1,-1], [0,-1], [1,-1]]
    for i in range(rows):
      for j in range(cols):
        neighbors = 0
        for d in directions:
          cell = np.array([i,j])+np.array(d)
          cell = (cell[0]%rows, cell[1]%cols)
          if prev_grid[cell] == 1:
            neighbors += 1
        cell = (i,j)
        check = (((game.grid[cell]==1) and (neighbors>=2 and neighbors<=3))
          or ((game.grid[cell]==0) and (neighbors!=3)))
        self.assertTrue(check)

  def test_after_100_runs(self):
      '''
      Verifying that all cells are obeying Conway's
      rules after RUNS number of updates
      '''
      game = Game()
      game.grid = np.array([          # Glider
          [1, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
      ])
      RUNS = 100
      for i in range(RUNS):
        game.updateGrid()
        if i==(RUNS-2):
          prev_grid = game.grid.copy()        
      rows, cols = game.grid.shape
      directions = [[1,0], [1,1], [0,1], [-1,1],
                    [-1,0], [-1,-1], [0,-1], [1,-1]]
      for i in range(rows):
        for j in range(cols):
          neighbors = 0
          for d in directions:
            cell = np.array([i,j])+np.array(d)
            cell = (cell[0]%rows, cell[1]%cols)
            if prev_grid[cell] == 1:
              neighbors += 1
          cell = (i,j)
          check = (((game.grid[cell]==1) and (neighbors>=2 and neighbors<=3))
            or ((game.grid[cell]==0) and (neighbors!=3)))
          self.assertTrue(check)

  def test_after_5_runs_for_toad(self):
      '''
      Verifying that all cells are obeying Conway's
      rules after RUNS number of updates
      '''
      game = Game()
      game.grid = np.array([          # Glider
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
      ])
      RUNS = 5
      for i in range(RUNS):
        game.updateGrid()
        if i==(RUNS-2):
          prev_grid = game.grid.copy()        
      rows, cols = game.grid.shape
      directions = [[1,0], [1,1], [0,1], [-1,1],
                    [-1,0], [-1,-1], [0,-1], [1,-1]]
      for i in range(rows):
        for j in range(cols):
          neighbors = 0
          for d in directions:
            cell = np.array([i,j])+np.array(d)
            cell = (cell[0]%rows, cell[1]%cols)
            if prev_grid[cell] == 1:
              neighbors += 1
          cell = (i,j)
          check = (((game.grid[cell]==1) and (neighbors>=2 and neighbors<=3))
            or ((game.grid[cell]==0) and (neighbors!=3)))
          self.assertTrue(check)

if __name__ == '__main__':
    unittest.main()