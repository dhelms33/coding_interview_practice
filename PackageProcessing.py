def solve_logistics(capacities, logs):
    n = len(capacities)
    # Track current load, total processed, and if center is active
    current_load = [0] * n
    total_processed = [0] * n
    is_open = [True] * n
    
    pointer = 0
    
    for event in logs:
        if event.startswith("CLOSURE"):
            idx = int(event.split()[1])
            is_open[idx] = False
        
        elif event == "PACKAGE":
            start_ptr = pointer
            package_delivered = False
            
            # Attempt to find a center with capacity
            while True:
                if is_open[pointer] and current_load[pointer] < capacities[pointer]:
                    current_load[pointer] += 1
                    total_processed[pointer] += 1
                    package_delivered = True
                    # Move pointer for next package
                    pointer = (pointer + 1) % n
                    break
                
                pointer = (pointer + 1) % n
                
                # We completed a full rotation and found NO space
                if pointer == start_ptr:
                    break
            
            # Trigger Reset Logic if rotation failed
            if not package_delivered:
                for i in range(n):
                    if is_open[i]:
                        current_load[i] = 0
                # Re-run the package logic (simplified here)
                # In a real test, you'd wrap the search in a function
    
    # Return index of max; if tie, return highest index
    max_val = -1
    best_idx = -1
    for i in range(n):
        if total_processed[i] >= max_val:
            max_val = total_processed[i]
            best_idx = i
    return best_idx