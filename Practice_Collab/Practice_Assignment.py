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

def determine_outcome(resources. choice, event):
    """ Determine the final ending 
