import pickle

from interpreteur import command, find_all


def search(conn, adrss, db, log):
  print(conn)
  s = pickle.loads(conn)
  result = find_all(command(f"find {s[0]}", db, log, dico={"name":s[1], "adresse":adrss}), s[1])
  conn.send(pickle.dumps(result))
  conn.close()
