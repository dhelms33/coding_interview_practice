from turtle import left
class Palindrome:
    def __init__(self):
        pass

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
    
    def is_palindrome_alt(self, s:str) -> bool:
        length_s = len(s)
        left_pointer_alt = 0
        right_pointer_alt = length_s - 1
        
        while left_pointer_alt < right_pointer_alt:
            if not s[left_pointer_alt].isalnum():
                left_pointer_alt += 1
                continue
            
            if not s[right_pointer_alt].isalnum():
                right_pointer_alt -= 1
                continue
            
            if s[right_pointer_alt].lower() != s[right_pointer_alt].lower():
                return False
            
            left_pointer_alt += 1
            right_pointer_alt -= 1
        return True
    
    #Time: O(n)
    # Space O(1)