#!/usr/bin/env python3

# trunc8 did this

import numpy as np
import os

class Helper:
  def clearConsole(self):
    '''
    Refresh terminal to print updated grid
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


  def conv2d(self,a, f):
    '''
    Using np only, no scipy dependency :)
    '''
    s = f.shape + tuple(np.subtract(a.shape, f.shape) + 1)
    strd = np.lib.stride_tricks.as_strided
    subM = strd(a, shape = s, strides = a.strides * 2)
    return np.einsum('ij,ijkl->kl', f, subM)


  def printGrid(self,mat, fmt=""):
    '''
    Pretty print
    '''
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
      for i, y in enumerate(x):
        symbol = '#'
        if y == 0:
          symbol = '-'
        print(("{:"+str(col_maxes[i])+fmt+"}").format(symbol), end="  ")
      print()

