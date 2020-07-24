import numpy as np
def find_factors(given_number):
    current_number = 1
    factors = []
    targeted_half = int(given_number/2)
    while((given_number > 1) and current_number <= targeted_half):
        if(given_number % current_number == 0):
            factors.append(current_number)
            factors.append(int(given_number/current_number))
        current_number += 1
    return factors 

print(np.unique(find_factors(8)))