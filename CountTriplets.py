def count_triplets(text: str) -> int:
    """_summary_

    Args:
        text (str): _description_

    Returns:
        int: number of triplets
    """
    if len(text) < 3:
        return 0
    
    count = 0
    # stop at len - 2 because we check i and i + 2
    for i in range(len(text)-2):
        if text[i] == text[i+2]:
            count+=1
    return count