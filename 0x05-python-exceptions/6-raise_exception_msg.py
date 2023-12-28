#!/usr/bin/python3
def raise_exception_msg(message=""):
  """ # This function will raise a NameError with the given message when called
      # It tries to use an undefined variable, which is not allowed in Python
  """
  x = undefined
  print(x + message)
