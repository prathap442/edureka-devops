given_list = [12,24,35,24,88,120,155]
after_removal_from_positions = []
removal_positions = [0,4,5]
for index,value in enumerate(given_list):
    if index not in removal_positions:
        after_removal_from_positions.append(value)

for value in after_removal_from_positions:
    print(value)