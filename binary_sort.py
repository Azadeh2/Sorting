import math

def binary_sort(my_numbers):
    """ binary sort halves the search inerval to find the correct position"""
    if not my_numbers or len(my_numbers) == 1: return my_numbers
    
    for current_ind in range(len(my_numbers)):
        hand = my_numbers[current_ind]
        if current_ind == 0: continue
        start_interval = 0
        end_interval = current_ind - 1
        cmp_ind = 0
        if_zero_start_end  = start_interval + end_interval

        while start_interval != end_interval and if_zero_start_end != 0:
            if end_interval - start_interval == 1:
                cmp_ind = int((start_interval + end_interval) / 2)
                
            elif (start_interval + end_interval) % 2 == 0:
                cmp_ind = int((start_interval + end_interval) / 2)
            else:
                cmp_ind = math.floor(int((start_interval + end_interval) / 2))
            
        
            if my_numbers[current_ind] > my_numbers[cmp_ind]:
                start_interval = cmp_ind + 1
                end_interval = end_interval
                # cmp_ind = start_interval
            
            else:
                start_interval =start_interval
                end_interval = cmp_ind
        cmp_ind = start_interval        
        
        # print(f'current index{current_ind} value {hand}, startInd {start_interval} end ind {end_interval} cmp {cmp_ind}')
        
        if hand >= my_numbers[cmp_ind]:
            new_placement = cmp_ind + 1
        else:
            new_placement = cmp_ind
        
        move_down_from = current_ind - 1
        # print(f'move down from {move_down_from}, new place {new_placement }')
        while move_down_from >= new_placement and my_numbers[move_down_from] > hand:
 
            my_numbers[move_down_from+1]= my_numbers[move_down_from]

            move_down_from = move_down_from - 1
            
        my_numbers[new_placement] = hand
    return my_numbers
print(binary_sort([1,3,4,5,2,6]))
print(binary_sort([2,1,4,5,2,6]))
print(binary_sort([6,5,4,3,2,1]))
print(binary_sort([1,2,3]))
print(binary_sort([8,7,6,9,10,1]))
print(binary_sort([0,10,6,9,3,1]))
print(binary_sort([1]))
print(binary_sort([]))
print(binary_sort([6,5,8,3,9,1]))