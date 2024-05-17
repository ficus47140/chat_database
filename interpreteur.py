import os


def int_convert(string):
  try:
    string.replace(",", " ")
    return int(string)
  except Exception:
    return None

def command(command, db, log, dico=None):
  open(log, "a+").write(f"command: {command}, {dico}\n")
  if command != "q":
    x = command.split(" ")
    if x[0] == "find":
      s = db.find_by_character(x[1])
      return s
    elif x[0] == "find_age":
      if len(x) >= 2:
        s = db.find_by_age(int_convert(x[1]), int_convert(x[2]))
        return s
      else:
        print("error : bad syntax")
    elif x[0] == "find_genre":
      if len(x) >= 2:
        s = db.find_by_genre(x[1])
        return s
      else:
        print("error : bad syntax")

    elif x[0] == "clear":
      os.system("clear")

    elif x[0] == "find_orientation":
      if len(x) >= 2:
        s = db.find_by_orientation(x[1])
        return s
      else:
        print("error : bad syntax")

def find_all(a, parametres):
  result = []
  for i, j in zip(parametres.keys(), parametres.values()):
    result = []
    for k in a:
      if (i == "name" and k.caract(j)) or (i == "age" and k.is_beetwen(j[0], j[1]) or (i == "genre" and k.find_by_genre(j))) or (i == "orientation" and k.find_by_orientation(j[0])):
        result.append(k)
    a = result
  return result
