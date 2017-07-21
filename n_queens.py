# Code to solve the n-Queens problem

from collections import Counter

def fitness(board_configuration):
    # Compute row attacks
    common_row_count = Counter(board_configuration)
    row_attacks = 0
    for item in common_row_count:
        if common_row_count[item] > 1:
            row_attacks += int((common_row_count[item]*(common_row_count[item]-1))/2)
            
    # Compute Column attacks: 0
    # Compute diagonal attacks  
    diagonal_attacks = 0
    for i in range(0,8):
        row_pos = int(board_configuration[i])
        upper_diagonal_pos = row_pos
        lower_diagonal_pos = row_pos
        for column_counter in range(i+1, 8):
            upper_diagonal_pos += 1
            lower_diagonal_pos -= 1
            if (int(board_configuration[column_counter]) == upper_diagonal_pos) or (int(board_configuration[column_counter]) == lower_diagonal_pos):
                diagonal_attacks += 1
                
    return 28 - row_attacks - diagonal_attacks
  
  