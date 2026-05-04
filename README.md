# College Life

## Overview
The purpose of this game is to allow users to play as a college student to experience events that occur in college. This game is a decision base game where the choices you pick determines your outcome. The choices will effect the student's health, money, GPA, and well-being. In order to complete the game you must run through a couple of events and pick the choice of 1 or 2 in response of the event. Throughout the game you will get a summary of your resources. At the end you will be told if you graduated college or not as well as your score.

## How to Run

## Step 1: Download the files required for the project.
Ensure you have all of the following files and have them in the same folder.
- `CollegeLife.py`
- `choices.json`
- `event_requirements.json`
- `game_config.json`

## Step 2: Open your terminal
Open the terminal and move into the folder you downloaded your files to using `cd`

Example:
```bash```
cd "/path/to/Practice_Collab

## Step 3: Run the game
Type in your terminal:

python3 CollegeLife.py **or** python CollegeLife.py

## How to Play
In CollegeLife, the player is a student in college who goes through a series of events where their outcome an effect their academic (GPA), soical life, money, and or extracurricular situation. For each event, the progam displays a short description and two numbered coices. The player responds by entering the number of option they want to select. After each event the program will display the summary of the resources. 

### Accepted Inputs
* Starting menu, the player must enter:
    * **1** to start the game
    * **2** to view the instructions
    * **3** to quit the game

* During the game, the player must enter:
    * **1** for the first choice
    * **2** for the second choice

If the player enters anything other than the allowed values, the program will display an eerror message and prompt the user again.

### How Stats Change

Each decision made affects one or more of the player's four main resources being:
 * **Health** - represents the player's physical well-being
 * **Money** - represents financial stability
 * **GPA** - reprsernts academic performance
 * **Emotion** - represents the player's mood and emotional well-being

Different choices increase or decrease these values by different amounts depending on the event. For example, if the player has an exam tomorrow but decide to go out that night. Their GPA will decrease but their emotions could increase. 

### Stat limits
* **Health** and **emotion** stays within the range of 0-100
* **GPA** stays within the range of 0.0 - 4.0
* **Money** can increase or decrease depending on the player's decison

### Game Over Conditions
The game could possibly end early if the player's resources falls below the stat limit. Otherwise, the player continues through all events until they recieve their final score and whether they graduated or not.

### Goal
The goal of the game is to make balanced life decison choices by managing their resources carefully enough to graduate with the best score outcome. 

# Data Files
```choices.json``` - stores event descriptions, player choices, and effects

```event_requirements.json``` - stores minimum GPA, cost, tags/categories

```game_config.json``` - stores starting resources, thresholds, and ending cutoffs

```events_requirements.json``` - stores the events requirements of minimal GPA and cost

```README.md``` - project docunmentation, usage instructions, and attributions.

# Techniques and Attribution
| display_resource_summary | Ruby Walsh | Optional Parameters/ keyword arguments |

| sort_events_by_impact | Ruby Walsh | key function: sorted() , lambda expression |

| determine_outcome | Junxi Chen | conditional expression |

| count_choice | Junxi Chen | comprehension expression |

| print_status | Duru Gokcen | f-strings , sequence unpacking |

| get_available_events | Adonis Hodges | set operations, regular expression |

# Bibliography

## Python Software Foundation. *json - JSON encoder and decoder.* 
https://docs.python.org/3/library/json.html 

Used to understand how to load and work with JSON data files in Python. 

## Python Software Foundaton. *os.path - Common pathname manipulations.* 
https://docs.python.org/3/library/os.path.html

Used to learn how to build file paths relative to the script location so the project can run on different computers. 

## Ruby Walsh **Walking Through** (unpublished Processing project, UMBC, 2022)

Used one of a group project I made in 2022 as reference for brainstorming the game structure, event flow, and decision-based interactions. The prior project helped inpsire the overall design and purpose of this test-based game.
