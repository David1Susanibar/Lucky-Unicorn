show_instructions = ""
while show_instructions != "xxx":


  show_instructions = input("have you played this game before?" ).lower()

  if show_instructions == "xxx":
    break
  elif show_instructions == "yes":
    print("program continues")
  elif show_instructions == "y":
    print("Program continues")
  
  elif show_instructions == "no":
    print("Display instructions")
  elif show_instructions == "n":
    print("Display instructions")
  else:
    print("Please answer yes / no")