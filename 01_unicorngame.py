show_instructions = input("have you played this game before?" ).lower()
if show_instructions == "yes" or show_instructions == "y":
  print("Program continues")


elif show_instructions == "no" or show_instructions == "n":
  print("Display instructions")

else:
  print("Please answer yes / no")