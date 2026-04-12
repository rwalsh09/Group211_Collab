def status_changes(resources, events, choice):
    """ Update the health, money, GPA, and emotion bar to either decrease
    depending on the user's choice during an event given. Each choice will
    lead to different outcomes which will have specific effects that change
    the level their status bar is on.
    
    The user will be prompted with a list of events going on that day as well as
    a list of choices they can choose from
    

    Args:
        resources (dict[str, int, float]): The current status values of emotion,
        money, GPA, and health.
        events (list): The prompt will create a lit of events that will
        influence the status bar to change and what their outcome will be.
        choice (list or int): The user's selected choice will determine the
        outcome and will then adjust the status adjustments.
    
    Returns:
        dict: The updated status bars (health, money, GPA, and emotions)
        with a scale of (0-100).
        
    Side Effects:
        Update the status value in the resources dictionary. 
    """
    events = [
        {
            "description": "You have a big exam tomorrow.",
            "choices": {
                1: {"health": - 10, "emotion": -8, "GPA": + 1.5},
                2: {"health": + 5, "emotion": + 4, "GPA": - 1}
            }
        },
        
           { "description": "Part-Time Job",
            "choices": {
                1: {"money": +30, "health": -10, "emotion": -5},
                2: {"money": 0, "health": +10, "emotion": +10} 
            }
        },
            
            {
                "description": "Join the Coding Club",
                "choices": {
                    1: {"money": - 20, "emotion": +15, "GPA": +0.4},
                    2: {"money": +15, "emotion": +10, "GPA": +.5, "health": -10}
                }
        },
            {
                "description": "National Honors Society",
                "choices":{
                    1: {"money": - 30, "emotion": +15, "GPA": +1},
                    2: {"money": -30, "emotion": +10, "GPA": +1, "health": -18}
                }
        },
            {
                "description": "Rest at Home",
                "choices":{
                    1: {"money": - 15, "emotion": +25, "health": +20},
                    2: {"money": 0, "emotion": +10, "health": -18}
                }
        },
            {
                "description": "Join the Football Team",
                "choices":{
                 1: {"money": - 40, "emotion": +8, "health": -25, "GPA": -1},
                 2: {"emotion": +10, "health": +10, "emotion": -12, "GPA": +.05}
            }
            
        }  
    ]
    
    resources = {
        "health": 100,
        "money": 100,
        "GPA": 4.0,
        "emotion": 100
    }
    
    for event in events:
        if choice == event["choice"]:
            
            changes = event["choices"][choice]
            
            # change each status bar
            for key in resources:
                
                # update status bar if event affects it
                if key in changes:
                    resources[key] += changes[key]
                if key == "GPA":
                    if resources[key] < 0.0:
                        resources[key] = 0.0
                    if resources[key] > 4.0:
                        resources[key] = 4.0
                else:
                
                    if resources[key] < 0:
                        resources[key] = 0
                    if resources[key] > 100:
                        resources[key] = 100
    return resources



def determine_outcome(resources, choice, event): 
    """Determine the final ending text based on the user's final resource levels
    and the last major choice made.

    Args:  
        resources (dict[str,int, float]): The  final resource value of emotions, money, gpa, 
        and health. 
            - "emotions" (float or int): The final emotional value.
            - "money" (float or int): The final amount of money.
            - "gpa" (float or int): The final GPA.
            - "health" (float or int): The final health status.
        choice (str): The key decision made by the player at the end of the game
            ("study for exams", "attend social event").
        event (str): The context or event in which the final choice was made
            ("exam week", "graduation party").

    Returns:
        str: A text ending description that reflects the combined outcome of
            resources and choices. Example: "You graduated but are deeply in debt
            and extremely stressed."
    """
    # Base score from final resources
    score = (resources["emotion"] * 0.2 +
             resources["money"] * 0.3 +
             resources["GPA"] * 10 +
             resources["health"] * 0.2)
    # Effects of different choices 
    streak = 0 
    for i in range(1, len(choice_history)):
        prev = choice_history[i-1]["choice_name"]
        curr = choice_history[i]["choice_name"]
        if prev == "study" and curr == "study":
            streak += 5
        if prev == "party" and curr == "study":
            score -= 10
    score += streak

    # Round and print final score
    rounded_score = int(round(score))
    print(f"Your final score is: {rounded_score}")
    
    # Determine ending based on score
    
    if rounded_score >= 80:
        return "You have graduated and ready for what comes moving forward."
    elif rounded_score >= 60:
        return "You have graduated but working hard for what comes next"
    elif rounded_score >= 40:
        return "You have barely graduated and with challenges moving forward"
    else:
        return "You did not graduate and rethinking what comes next"

def check_game_over(resources):
    """
    Checks if the game should end based on the player's status levels 

    The game ends if an important status, like GPA, health, money,
    or emotion, falls below a required minimum value.

    Args:
        resources (dict[str, int | float]): A dictionary containing the
            player's current values:
            {
                "GPA": float (0.0–4.0),
                "money": int,
                "health": int (0–100),
                "emotion": int (0–100)
            }

    Returns:
        bool: True if the game is over, False if the player can continue.

    Raises:
        ValueError: If required resource values are missing.
    """
    required_keys = ["GPA", "money", "health", "emotion"]
    
    # check if all required keys exist
    for key in required_keys:
        if key not in resources:
            raise ValueError("Missing resource: " + key)

    # check game over conditions
    for key, value in resources.items():
        if key == "GPA" and value < 1.0:
            return True
        if key == "health" and value < 20:
            return True
        if key == "emotion" and value < 10:
            return True
        if key == "money" and value < 0:
            return True

    return False

def get_available_events(gpa, **resources):
    """
    Checks what possible events the player can do based on game performance.
    Filters possible game events based on requirements.
    
    Args:
        gpa (float): The current GPA (0.0 - 4.0).
        **resources: Keyword arguments like money=100 or health=80.

    Returns:
        dict: A dictionary of eligible options and status 
    """
    
    events = {
        "National Honors Society": {"min_gpa": 3.5, "cost": 0},
        "Coding Club": {"min_gpa": 3.0, "cost": 20},
        "Part-time Job": {"min_gpa": 2.0, "cost": 0},
        "Rest at Home": {"min_gpa": 0.0, "cost": 0},
        "Join the Football Team": {"min_gpa": 2.5, "cost": 50}
    }
    
    event_pool = events.keys()

    current_money = resources.get('money', 0)
    
    eligible_events = {
        name for name in event_pool 
        if gpa >= events[name]["min_gpa"] 
        and current_money >= events[name]["cost"]
    }
    
    sorted_options = sorted(
        eligible_events, 
        key=lambda x: events[x]["min_gpa"], 
        reverse=True
    )

top_choice = sorted_options[0] if sorted_options else "No events available"

print(f"Outcome: {top_choice.upper()}")

return {
     "player_options": sorted_options,
        "gpa_status": "Dean's List" if gpa >= 3.5 else "Good"
}

