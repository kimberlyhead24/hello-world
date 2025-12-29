import re

def format_names(names):
  # pattern: Lastname, Firstname  ->  Firstname Lastname
  pattern = r"^([\w .-]*),\s*([\w .-]*)$"
  replacement = r"\2 \1"


  # apply re.sub to every name in the list
  converted_names = [re.sub(pattern, replacement, name) for name in names]

  return converted_names


names1 = [
    "Lovelace, Ada",
    "Turing, Alan",
    "Hopper, Grace",
    "Johnson, Katherine"
]
format_names(names1)
