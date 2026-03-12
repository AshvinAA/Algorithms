def kadanes_algorithm(net_goal_difference):
    
    if not net_goal_difference:
        return 0
        
    current_streak = net_goal_difference[0]
    global_best = net_goal_difference[0]
    

    for i in range(1, len(net_goal_difference)):
        num = net_goal_difference[i]
        
       
        current_streak = max(num, current_streak + num)
        
        
        global_best = max(global_best, current_streak)
        
    return global_best


matches = [1, 4, 3, -5, 5, 6, 1, -4]
print(f"Best consecutive performance: {kadanes_algorithm(matches)}") 
