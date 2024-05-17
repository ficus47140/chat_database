from unit import Unit

class Database:
  def __init__(self, n_row : int):
    self.n_row, self.full = n_row, False
    self.content = []

  def stock(self, content):
    if len(self.content) >= self.n_row:
      #raise Exception("error : full capacity reached")
      self.full = True
    else:
      self.content.append(content)

  def find_by_name(self, name):
    result = []

    for i in self.content:
      if name in i.name:
        result.append(i)

    return result

  def find_by_content(self, name):
    result = []

    for i in self.content:
      if i.caract(name):
        result.append(i)

    return result

  def find_by_age(self, first, second):
    result = []

    for i in self.content:
      if i.is_beetwen(first, second):
        result.append(i)

    return result

  def find_by_genre(self, genre):
    result = []
    for i in self.content:
      x = i.find_by_genre(genre)
      if x:
        result.extend([x])
    return result

  def find_by_orientation(self, genre):
    result = []
    for i in self.content:
      x = i.find_by_orientation(genre)
      if x:
        result.extend([x])
    return result

"""database = Database(10)

database.stock(Unit("moi", "bonjour, je suis moi", 16))
database.stock(Unit("quelqu'un", "bonjour, je suis quelqu'un", 32))

print(database.find_by_age(10, 18))
print(database.find_by_content("moi"))
print(database.find_by_name("q"))
"""
