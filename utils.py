s = "2300. Successful Pairs of Spells and Potions"
splits = s.split(". ")
level = ["easy", "medium", "hard"]

questions = splits[1].replace(" ", "_").lower()
numbers = splits[0]

result = f"{questions}_{level[1]}_{numbers}"

print(result)