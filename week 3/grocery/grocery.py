groceryList = []

while True:
   try:
      inp = input("")
      groceryList.append(inp)
   except:
       break

groceryList.sort()

for i,item in enumerate(groceryList):
   fruit = item
   print(f"{groceryList.count(item)} {item.upper()}")

   if groceryList.count(item) > 1:
      for i,fruit in enumerate(groceryList):
         if fruit == item:
            groceryList.pop(i)