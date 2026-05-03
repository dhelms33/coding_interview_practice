def get_digital_root(n: int) -> int:
    # get root
    while n >= 10:
        current_sum = 0
        while n > 0:
            current_sum += n % 10 # Get last digit
            n //= 10              # Remove last digit
        n = current_sum
    return n
#helper function that returns the max digital root
def max_digital_root(nums: list[int]) -> int:
    if not nums: return 0
    return max(get_digital_root(x) for x in nums)