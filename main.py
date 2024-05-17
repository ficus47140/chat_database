import os
import pickle
import random
import socket

from database_unit import Database
from search import search
from unit import Unit

class full_database:
  def __init__(self, first_database:Database, n_row, case):
    self.content = [first_database]

    self.n_row = n_row
    self.case = case

  def load(self):
    for i in os.listdir(self.case):
      yield pickle.load(open(f"{self.case}/{i}", "rb"))

  def update(self):
    if self.content[-1].full:
      self.content.append(Database(self.n_row))
      self.save()

  def stock(self, user, content, age, genre, orientation):
    self.content[-1].stock(Unit(content, user, age, genre, orientation))
    self.update()

  def find_by_character(self, user):
    result = []
    for i in self.load():
      x = i.find_by_content(user)
      if x:
        result.extend(x)
    return result

  def find_by_age(self, a, b):
    result = []
    for i in self.load():
      x = i.find_by_age(a, b)
      if x:
        result.extend(x)
    return result

  def find_by_genre(self, genre):
    result = []
    for i in self.load():
      x = i.find_by_genre(genre)
      if x:
        result.extend(x)
    return result

  def save(self):
    with open(f"{self.case}/{len(os.listdir((self.case)))+1}.pickle", "wb") as file:
      pickle.dump(self.content[0], file)
      del self.content[0]

  def block(self, username):
    for i, j in zip(self.load(), range(1, len(os.listdir(self.case)))):
      if i.find_username(username):
        i.block_by_username(username)
        with open(f"{self.case}/{j}.pickle", "wb") as file:
          pickle.dump(i, file)

  def reset(self):
    for i in os.listdir(self.case):
      os.remove(f"{self.case}/{i}")

  def find_by_orientation(self, orientation):
    result = []
    for i in self.load():
      x = i.find_by_orientation(orientation)
      if x:
        result.extend(x)
    return result

db = full_database(Database(20), 20, "data")
db.reset()
orientation = ["Hétérosexuel", "Homosexuel", "Bisexuel", "Pansexuel", "Asexuel", "Aromantique", "Autre"]

for i in range(1000):
  db.stock("user", "username", i, random.choice(["femme", "homme", "non-binaire"]), random.choice(orientation).lower())

adrs = 1234
print(socket.gethostbyname(socket.gethostname()))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostbyname(socket.gethostname()), adrs))

sock.listen()
while True:
  client, adrss = sock.accept()
  search(client.recv(4096), adrss, db, "log.txt")

