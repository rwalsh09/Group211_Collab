# Ruby
def starting_screen():
    """Generates a welcome screen for the user.
    """
    while True:
        print("Welcome To College Life")
        print("1. Start Game")
        print("2. Instructions")
        print("3. Quit")
        
        choice = input("Choose an option: ")
        
        if choice in ("1", "2", "3"):
            return choice
        else:
            print("You must enter 1, 2, or 3!\n")

# Ruby
def status_changes(resources, event, choice):
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
    #for event in events:
    if choice in event["choices"]:
            
            changes = event["choices"][choice]["effects"]
            
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
                        
                elif key in ["health", "emotion"]:
                    if resources[key] < 0:
                        resources[key] = 0
                    if resources[key] > 100:
                        resources[key] = 100
                        
                        # money bar has no limit because get that money
                    else:
                        pass
    return resources

# Ruby
def get_choices():
    """This will show the two choices the user can pck from.

    Returns:
        list: List displays the choices the user can pick for the outcome of the
        event.
    """
    return [
        {
            "description": "You have a big exam tomorrow.",
            "choices": {
                1: {
                    "text":"I'll just stay in and study! I need to pass.",
                    "effects":{"health": - 10, "emotion": -8, "GPA": + 1.5}
                },
                2: {
                    "text":"My friend asked me to hangout... I should be good.",
            "effects":{"money": -18, "health": + 5, "emotion": + 4, "GPA": - 1}
                }
            }
        },
        
           { "description": "Part-Time Job",
            "choices": {
                1: {
                    "text":"I'm so happy I was hired at Raise N' Canes!",
             "effects":{"money": +40, "health": -10, "emotion": +6, "GPA": -.5}
                },
                2: {
                    "text": "I don't have time for part-time. I'll just wait.",
                "effects":{"money": 0, "health": +10, "emotion": +1,"GPA": +.3}
                } 
            }
        },
            
            {
                "description": "Join the Coding Club",
                "choices": {
                    1: {
                        "text":"I'll join the club, why a fee though?",
        "effects":{"money": - 20, "emotion": +15, "GPA": +0.4, "health": -1},
                    },
                    2: {
                        "text": "I don't really need to join a club.",
                        "effects":{"money":0, "emotion": +10, "GPA":-.3}
                    }
                }
            },
            {
                "description": "National Honors Society",
                "choices":{
                    1: {
                        "text":"This would look great on my resume.",
                        "effects":{"money": - 30, "emotion": +15, "GPA": +1}
                    },
                    2: {
                       "text":"I'll pass, I don't need this for my resume.",
             "effects": {"money": -30, "emotion": +10, "GPA": +1, "health": -18}
                    }
                }
            },
            {
                "description": "Rest at Home",
                "choices":{
                    1: {
                    "text":"My friend asked me to go out, why not it's Friday.",
                        "effects":{"money": - 15, "emotion": +12, "health": +20}
                    },
                    2: {
                        "text":"I need to save money, I'll just stay in.",
                        "effects":{"money": 0, "emotion": +10, "health": -18}
                    }
                }
        },
            {
                "description": "Join the Football Team",
                "choices":{
                 1: {
                 "text":"Wow, I can't believe I made it trough try outs!",    
            "effects":{"money": - 40, "emotion": +8, "health": -25, "GPA": -1}  
                },
                 2: {
                "text":"I don't want to get injured, I'll join another sport.",     
                "effects":{"health": +10, "emotion": +10}
                 }
            }
            
        }  
    ]

#Junxi -> count_choice && determine_outcome
def count_choice(choice_history, choice_name):
    """Return count of a specific choice type using a list comprehension
    Returns:
        int: Number of times that choice will appear in the history
    """
    
    return len([choice for choice in choice_history if choice[
        "choice_name"] == choice_name])

# def determine_outcome(resources, choice, event): 
def determine_outcome(resources, choice_history): 
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
    #List Comprehension: Create a list of only study choices
    study_count = count_choice(choice_history, "study")
    
    #Conditional Expression: Gives bonus if number of study sessions is >3
    bonus = 3 if study_count > 2 else 0
    
    # Base score from final resources
    score = (resources["emotion"] * 0.2 +
             resources["money"] * 0.3 +
             resources["GPA"] * 10 +
             resources["health"] * 0.2)
    #Bonus add if condition is met
    score += bonus
    
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

# keyword argument/ optional parser (Ruby Walsh)
def display_resource_summary(resources, title=True):
    """This will generate a summary of the player's current status bar
    level. The title=True is a optional parameter that controls
    if the header is printed.
    """
    
    if title:
        print("Current Player Resources:")
        
    print(f"Health: {resources['health']}")
    print(f"Money: {resources['money']}")
    print(f"GPA: {resources['GPA']}")
    print(f"Emotion: {resources['emotion']}")
    
# sorted() lambda (Ruby Walsh)
def sort_events_by_impact(events):
    """Sort events based on their overall impact on player's stats.
    """
    
    def total_change(event):
        return sum(abs(v) for v in event["choices"][1]["effects"].values())
    
    return sorted(events, key=lambda e: total_change(e), reverse=True)

#Ruby

def get_valid_event_choice():
    """If the user types anything but 1 or 2 for the choices, results in error.
    """
    while True:
        choice = input("Choose 1 or 2: ")
        
        if choice in ("1", "2"):
            return int(choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")
            
# Ruby
def play_game():
    resources = {
            "health": 100,
            "money": 100,
            "GPA": 4.0,
            "emotion": 100
        }
    choice_history = []
    
    events = get_choices()
    
    for event in events:
            print("\nEvent:", event["description"])
            print("1:", event["choices"][1]["text"])
            print("2:", event["choices"][2]["text"])
            
            choice = get_valid_event_choice()
            
            if choice == 1:
                choice_history.append({"choice_name": "study"})
            else:
                choice_history.append({"choice_name": "party"})
                
            resources = status_changes(resources, event, choice)
            
            display_resource_summary(resources)
            
            if check_game_over(resources):
                print("\nGame Over! Your stats dropped too low.")
                break
        
    print("Final Outcome: ")
    ending = determine_outcome(resources, choice_history)
    print(ending)


# Ruby
if __name__ == "__main__":
    
    while True:
        user_choice = starting_screen()
        
        if user_choice == "1":
            play_game()
            
        elif user_choice == "2":
            print("\nInstructions:")
            print("Play through the lens of a college student.")
            print("Make choices that affect your GPA, money, health, and emotions.")
            print("Good Luck!")
            play_game()
        
        elif user_choice == "3":
            print("Play Again Soon!")
            exit()
        
        elif user_choice not in ("1", "2", "3"):
            print("You must enter 1, 2 or 3!")
