def find_max_sum_subarray(lst): 
  if (len(lst) < 1): 
    return 0;

  curr_max = lst[0];
  global_max = lst[0];
  length_array = len(lst);
  for i in range(1, length_array):
    if curr_max < 0: 
      curr_max = lst[i]
    else:
      curr_max += lst[i]
    if global_max < curr_max:
      global_max = curr_max

  return global_max;
