from sqlalchemy import null


def first_duplicate(nums: list[int]) -> int:
    seen = {}
    
    for num in nums:
        if num in seen:
            return num #first one to repeat
        seen[num] = True
    return 0