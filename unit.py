class Unit:
  def __init__(self, name, content, age:int, genre, orientation):
    self.name, self.content, self.age, self.genre = name, content, age, genre
    self.orientation = orientation

  def __str__(self):
    return f"Personne: {self.name}, âge: {self.age}, content: {self.content}"

  def is_beetwen(self, first, second):
    if self.age <= max(first, second) and self.age >= min(first, second):
      return True
    return False

  def caract(self, caract):
    if caract in self.content:
      return True
    return False 

  def find_by_genre(self, genre):
    if genre == self.genre:
      return self
    return None

  def find_by_orientation(self, orientation):
    if orientation == self.orientation:
      return self
    return None

  