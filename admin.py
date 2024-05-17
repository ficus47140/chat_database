from interpreteur import command

admin = ""
while admin != "q":
  admin = input(">>>")
  x = command(admin, db, "log.txt", dico={None:None})
  if x:
    user = input(f"{len(x)} resultats trouvés. voulez vous les voir ? (y/n)")
    if user == "y":
      for i in x:
        print(str(i))
    else:
      print("vos desirs sont des ordre")

