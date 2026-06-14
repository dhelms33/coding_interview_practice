from turtle import left


def is_palindrome_str(s:str)-> bool:
    """ return True or False if the string reads the same forwards as backwards"""
    #edge case handling
    if not isinstance(s,str):
        raise TypeError("input string must be of type string. Please try encapsulating your input with quotes")
    # cleaned string that eliminates 
    cleaned_str = "".join(char.lower() for char in s if char.isalnum())
    
    #initialize pointers
    left_pointer = 0
    right_pointer = len(cleaned_str)-1
    
    while left_pointer < right_pointer:
        if cleaned_str[left_pointer] != cleaned_str[right_pointer]:
            return False #mismatch identified
        left_pointer += 1
        right_pointer -= 1
    return True
    