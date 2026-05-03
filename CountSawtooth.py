def count_sawtooth(arr: list[int]) -> int:
    if not arr: return 0
    
    total_count = 0
    current_streak_length = 1
    
    for i in range(1, len(arr)):
        # Check if parity alternates (Even/Odd or Odd/Even)
        if (arr[i] % 2) != (arr[i-1] % 2):
            current_streak_length += 1
        else:
            # Streak broke! Add the combinations for the completed streak
            total_count += (current_streak_length * (current_streak_length + 1)) // 2
            current_streak_length = 1 # Reset to 1 (the current element itself)
            
    # Add the final streak
    total_count += (current_streak_length * (current_streak_length + 1)) // 2
    return total_count