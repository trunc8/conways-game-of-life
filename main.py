#!/usr/bin/env python3

# trunc8 did this

import numpy as np
import os
import time

from game_core import Game


if __name__ == '__main__':
  try:
    game = Game()
    game.startGame()
  except:
    print("\nExiting...")