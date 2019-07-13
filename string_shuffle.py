## String Suffle

import random
def shuffle(input_str):
  input_arr = list(input_str)
  cur_index = 0
  input_str_len = len(input_arr)
  
  for i in range(0, input_str_len):
    random_index = int(random.random()) * (input_str_len - i) + i
    temp = input_arr[i]
    input_arr[i] = input_arr[random_index]
    input_arr[random_index] = temp
  
  return ''.join(input_arr)


def do_lenth_match():
  input_str = "ramesh godishela"
  result = shuffle(input_str)
  
