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

def determine_outcome(resources, choice, event) 
    """Determine the final ending text based on the user's final resource levels
    amd the last major choice made.

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


def check_game_over(resources):
    """
    Checks if the game should end based on the player's current status levels.

    The game ends if an important status, like GPA, health, money,
    or emotions, falls below a required minimum value. This function
    helps determine whether the player can continue playing or has lost.

    Args:
        resources (dict[str, int | float]): A dictionary containing the
            player's current values for GPA, health, money, and emotions.

    Returns:
        bool: True if the game is over, False if the player can continue.
        

    Raises:
        ValueError: If required resource values are missing.
    """
