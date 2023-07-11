row1 = ["🟥","🟥","🟥"]
row2 = ["🟥","🟥","🟥"]
row3 = ["🟥","🟥","🟥"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to pu the treasure ?")
horizontal = int(position[0])
vertical = int(position[1])

map[horizontal-1][vertical-1] = "X"

print(f"{row1}\n{row2}\n{row3}")