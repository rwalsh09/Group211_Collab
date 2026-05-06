import re
import json
import os

def load_json(filename):
    """Load and return the data from the JSON files.
    
    Args:
        filename (str): The name of the JSON file to load.
        
    Returns:
        dict or list: The parsed JSON data from the file.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file does not contain valid JSON.
        
    Side Effects:
        Reads a JSON file from disk.
        
    Primary author: Ruby Walsh
    Technique claimed: JSON files.
    """
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
    
class CampusActivity:
    """Represent a general campus activity with cost and GPA requirements.
    
    Attributes:
        name (str): The name of the activity.
        min_gpa (float): The minimum GPA required for the activity.
        cost (int or float): The cost of the activity. 
    
    Primary author: Ruby Walsh
    Technique claimed: class.
    """
    
    def __init__(self, name, min_gpa, cost):
        """Initialize a CampusActivtiy.

        Args:
            name (str): The name of the activity.
            min_gpa (float): The minium GPA required.
            cost (int or float): The cost to participate. 
        
        Returns:
            None
            
         Side Effects:
            Intializes the instance attributes "name", "min_gpa", and "cost"
        """
        self.name = name
        self.min_gpa = min_gpa
        self.cost = cost
        
    def activity_info(self):
        """Return a formatted information about the activity.
        
        Returns:
            str: A sentence describing the activity's GPA requirement and cost.
        """
        return f"{self.name} requires GPA {self.min_gpa} and costs ${self.cost}."
    

class ClubActivity(CampusActivity):
    """Represents a club based activity that inherits from CampusActivity
    
    Attributes:
        category (str): The type of caegory of club activity.
    
    Primary Author: Ruby Walsh
    Technique claimed: inheritance.
    """

    def __init__(self, name, min_gpa, cost, category):
        """Intialize a ClubActivity.

        Args:
            name (str): The name of the club activity.
            min_gpa (float): The minimum GPA required.
            cost (int or float): The cost to partcipate.
            category (str): The type of activity.
        
        Returns:
            None
            
        Side Effects:
            Intalizes inherited instance attributes and sets category. 
        """
        super().__init__(name, min_gpa, cost)
        self.category = category
    
    def activity_info(self):
        """Returns club activity information.

        Returns:
            str: Displays the name, category, and required GPA and cost. 
        """
        return (
        f"{self.name} is a {self.category} activity, requires GPA "
        f"{self.min_gpa}, and costs ${self.cost}"
        )
        
        
def starting_screen():
    """Generates a welcome screen for the user and return the user's selected
    choices.
    
    The menu allows the user to start the game, view instructions, or quit the
    program.
    
    Returns:
        str: The user's validated menu selction as "1", "2", "or "3".
        
    Side Effects:
        Prints menu text to standard output and reads user input from 
        standard input.
    
    Primary author: Ruby Walsh
    Technique claimed: n/a for this function.
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
        Update the resources dictionary by updating health, GPA, and emotion
        values. 
        
    Primary author: Ruby Walsh
    Technique claimed: n/a for this function, main algorithimic function.
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


def get_choices():
    """This load choices from a JSON file.
    
    This function reads the event data from the JSON file and converts the data
    into integers to then be consistently used throughout the program.

    Returns:
        list[dict]: List displays the choices the user can pick 
        for the outcome of the event.
    
    Side Effects:
        Reads event data from disk and changes each event's choices dictionary
        by converting its keys from strings to integers. 
        
    Primary author: Ruby Walsh
    Technique claimed: n/a for this function.
    """

    events = load_json("choices.json")
    
    for event in events:
        event["choices"] = {int(k): v for k, v in event["choices"].items()}
        
    return events


def count_choice(choice_history):
    """Counts events of each choice type in the history.
    
    Args:
        choice_history (list[dict]): A list of dictionaries representing 
        previous player choices.
        
    Returns:
        dict[str, int]: A dictionary contianing the counts for each choice
        type.

    
        Primary author: Junxi Chen
        Technique claimed: comprehensions. 
    """
    #comprehensions
    choice_types = {"study", "party"} 
    return {
        choice: len([c for c in choice_history if c["choice_name"] == choice])
        for choice in choice_types
    }
    
    

def determine_outcome(resources, choice_history): 
    """Determine the final ending text based on the user's final resource levels
    and the last major choice made.
    
    Args:  
        resources (dict[str,int, float]): The  final resource value of emotions, 
        money, gpa, and health. 
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
    
    Side Effects:
        Prints the final score to standard output and reads ending thresholds
        from "game_config.json".
        
    Primary author: Junxi Chen
    Technique claimed: conditional expession and main aglorithimic function.
    """
    #List Comprehension: Create a list of only study choices
    counts = count_choice(choice_history)
    study_count = counts["study"]    
    
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

    # Round and print final score2
    rounded_score = int(round(score))
    print(f"Your final score is: {rounded_score}")
    
    # Determine ending based on score
    
    config = load_json("game_config.json")
    endings = config["ending_thresholds"]
    
    if rounded_score >= endings["excellent"]:
        return "\n You have graduated and ready for what comes moving forward.\n"
    elif rounded_score >= endings["good"]:
        return "\n You have graduated but working hard for what comes next\n"
    elif rounded_score >= endings["barely"]:
        return "\n You have barely graduated and with challenges moving forward\n"
    else:
        return "\n You did not graduate and rethinking what comes next\n"


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
        
    Side Effects:
        Reads game-over thresholds from "game_config.json".
        
        Primary author: Duru Gokcen
        Technique claimed: n/a for this function, main algorithimic function.
    """
    required_keys = ["GPA", "money", "health", "emotion"]
    
    # check if all required keys exist
    for key in required_keys:
        if key not in resources:
            raise ValueError("Missing resource: " + key)

    # check game over conditions
    config = load_json("game_config.json")
    thresholds = config["game_over_thresholds"]
    
    for key, value in resources.items():
        if key in thresholds and value < thresholds[key]:
            return True
    
    return False


def print_status(resources):
    """
    Prints the player's current GPA, money, health, and emotion levels.

    Args:
        resources (dict[str, int | float]): Player stats.

    Returns:
        None
        
    Side Effects:
        Prints resource values to standard output.
        
    Primary author: Duru Gokcen
    Technique claimed: f-strings, sequence unpacking
    """

    # sequence unpacking
    for key, value in resources.items():
        # f-strings
        print(f"{key}: {value}")


def get_available_events(gpa, **resources):
    """
    Filters and ranks game events based on players current assets such as
    GPA and money. Can be used to search for team based or group centered clubs
    and activities.

    Args:
        gpa (float): The player's current Grade Point Average (0.0 to 4.0 scale).
        **resources: Keyword arguments such as money.

    Returns:
        dict: A dictionary of eligible options and status.
        
    Side Effects:
        Reads event requirements from disk and prints activity information
        and outcome text to standard output.
        
    Primary author: Adonis Hodges
    Technique claimed: Set operations and regular expressions.
    """
    
    events = load_json("event_requirements.json")
    sample_activity = ClubActivity(
        "Coding Club", events["Coding Club"]["min_gpa"],
        events["Coding Club"]["cost"], "Club"
    )
    print(sample_activity.activity_info())
    
    #set operation (intersection)
    featured_events = {"Coding Club", "Join the Football Team", "National Honors Society"}
    available_events = set(events.keys()) & featured_events
    
    #regular expressions (Team based)
    regex_pattern = r"Club|Society|Team"
    filtered_by_regex = {
        name for name in available_events 
        if re.search(regex_pattern, name)
    }
    
    current_money = resources.get('money', 0)

    #set comprehension
    eligible_events = {
        name for name in filtered_by_regex
        if gpa >= events[name]["min_gpa"] 
        and current_money >= events[name]["cost"]
    }

    #lambda sorted()
    sorted_options = sorted(
        eligible_events, 
        key=lambda x: events[x]["min_gpa"], 
        reverse=True
    )

    #conditional expression
    top_choice = sorted_options[0] if sorted_options else "No events available"

    #f-string
    print(f"\nOutcome: {top_choice.upper()}")

    return {
        "player_options": sorted_options,
        "gpa_status": "Dean's List" if gpa >= 3.5 else "Good"
    }


def display_results(results):
    """
    Prints the player's available event options and their academic status.

    Args:
    results (dict): A dictionary containing player_options (list) 
    and gpa_status (str).

    Returns:
        None
    
    Side Effects:
        Prints event options and acaedmic status to standard output.
    
    Primary author: Adonis Hodges
    Technique claimed: n/a for this function.
    """
    options = results.get("player_options", [])
    status = results.get("gpa_status", "Standard")

    print("--- AVAILABLE OPPORTUNITIES ---")
   
  
    if not options:
        print("No matches found. Try focusing on your studies instead of parties!")
    #f-string
    else:
        for activity in options:
            print(f"- {activity}")

#conditonal statement
    if status == "Dean's List":
        print(f"\nKeep going! You're currently on {status}, don't mess it up!")
    else:
        print(f"\nStatus: {status}")
        

def display_resource_summary(resources, title=True):
    """This will generate a summary of the player's current status bar
    level. The title=True is a optional parameter that controls
    if the header is printed.
    
    Args:
        resources (dict[str, int or float]): The player's current health, money,
            GPA, and emotion values.
        title (bool): If True, print a "Resources:" header before the summary.
            Defaults to True.
    
    Returns:
        None
        
    Side Effects:
        Prints a formatted resource summary to standard output.
    
    Primary author: Ruby Walsh
    Technique claimed: keyword argument/ optional parser.
    
    """
    
    if title:
        print("\n")
        print("Resources:")
        
    print(f"Health: {resources['health']}")
    print(f"Money: {resources['money']}")
    print(f"GPA: {resources['GPA']}")
    print(f"Emotion: {resources['emotion']}")
    
    
def sort_events_by_impact(events):
    """Sort events based on their overall impact on player's stats.
    
    Args:
        events (list[dict]): A list of event dictionaries.
    
    Returns:
        list[dict]: The events sorted in descending order by total effect size.
        
        
        Primary author: Ruby Walsh
        Technique claimed: sorted() with lambda function.
    """
    
    def total_change(event):
        return sum(abs(v) for v in event["choices"][1]["effects"].values())
    
    return sorted(events, key=lambda e: total_change(e), reverse=True)


def get_valid_event_choice():
    """ If the user types anything but 1 or 2 for the choices, results in error.
    
    Returns:
        int: The validated choice number of either "1" or "2".
        
    Side Effects:
        Reads user input from standard input and prints validation messages
        to standard output.
    
    Primary author: Ruby Walsh
    Technique claimed: n/a for this function.
    """
    while True:
        choice = input("\nChoose 1 or 2: ")
        
        if choice in ("1", "2"):
            return int(choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")
            

def play_game():
    """ Run one full loop of the College Life game.
    
    This function will load the starting configuration, process each event,
    update the resources based off the palyer's choice, check if the game ended
    conditions, and display the final outcome.
    
    Returns:
        None
    
    Side Effects:
        Reads configuration and event data from disk, prints the game progress
        and outcome text to standard output, and prompts the user for input
        through the helper functions. 
        
    Primary author: Ruby Walsh
    Technique claimed: n/a for this function.
    """
    config = load_json("game_config.json")
    resources = dict(config["starting_resources"])
        
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
        
    print("\nFinal Outcome: ")
    ending = determine_outcome(resources, choice_history)
    print(ending)


if __name__ == "__main__":
    while True:
        user_choice = starting_screen()
        
        if user_choice == "1":
            play_game()
            
        elif user_choice == "2":
            print("\nInstructions:")
            print("Play through the lens of a college student.")
            print("Make choices that affect your GPA, money, health, and emotions.")
            print("Select choice by selecting 1 or 2.")
            print("Good Luck!")
            play_game()
        
        elif user_choice == "3":
            print("\nPlay Again Soon!")
            exit()
        
        elif user_choice not in ("1", "2", "3"):
            print("\nYou must enter 1, 2 or 3!")
