'''
==================================================================
hurrr by Alex Levenson

Utilities for interacting with the filesystem
=================================================================
'''

import os
import random

class NotADirectoryError(Exception):
    pass

def generateUniqueFileName(dir, extension, prefix="", randSpace=100000000000):
  '''
  return: a filename that does not exist in dir that begins with prefix
  if <prefix>.<extension> does not exist, then it is used.
  extension.lower() will bue used as the extension
  '''

  extension = extension.lower()

  if prefix and not os.path.exists(os.path.join(dir, prefix + extension)):
    return prefix + extension

  f = prefix + "_" + str(random.randint(0, randSpace)) + extension
  while os.path.exists(os.path.join(dir, f)):
    f = prefix + "_" + str(random.randint(0, randSpace)) + extension
  return f

def ensureDirectoryExists(dirPath):
  '''
  Checks that:
      1) dir_path exists
      2) dir_path is a directory

  If dir_path does not exist, tries to create it

  dir_path: path to the directory being checked / created

  raises OSError: if dir_path does not exist and cannot be created

  raises NotADirectoryError: if dir_path exists but is not a directory
  '''

  if not os.path.exists(dirPath):
    # this may raise an OSError
    os.makedirs(dirPath)

  if not os.path.isdir(dirPath):
    raise NotADirectoryError(dirPath)
