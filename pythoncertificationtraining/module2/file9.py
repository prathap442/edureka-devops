given_list = [12,24,35,70,88,120,155]
residue_list = []
for num in given_list:
    if not((num%5 == 0) or (num%7==0)):
        residue_list.append(num)
print(residue_list)