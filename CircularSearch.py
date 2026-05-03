def circular_search(lst: list[str])->list[str]:
    """
    given a list, use a while loop and % to print the elements in order and then stop
    Args:
        lst (list[str]): _description_
    """
    #edge case
    
    if not lst:
        return [""]
    #initialize variables
    n = len(lst)
    current_step = 0
    total_steps = n * 2
    result = []
    
    
    while current_step < total_steps:
        index = current_step % n
        result.append(lst[index])
        current_step += 1
    return result

print(circular_search(["two","one", "Three"]))