import random
from datetime import date

# Variables to be used by meal_selector()
meal_options = ["Brunch", "Lunch", "Dinner", "claudio", "dennelise"]

# Variables to be used by cuisine_selector()
cuisine_options = ["claudio", "dennelise", "Italian", "Chinese", "Japanese", "Portuguese", "Mexican", "Korean", "Burguer", "French"]

# Variables to be used by new_or_repeated()
new_repeated = ["New", "Repeated"]

#Variables to be used by history()
history_logs = []

# Function that randomly selects the meal
def meal_selector():
    meal_selection = random.choice(meal_options)
    
    text_meal = ""

    if meal_selection == "claudio":
        text_meal = "Next week's date meal will be chosen by Claudio "
    elif meal_selection == "dennelise":
        text_meal = "Next week's date meal will be chosen by Dennelise "
    else:
        text_meal = "Next week's date will be a " + meal_selection

    return text_meal, meal_selection

# Function that randomly selects the cuisine

def cuisine_selector():
    cuisine_selection = random.choice(cuisine_options)

    text_cuisine = ""

    if cuisine_selection == "claudio":
        text_cuisine = ", the cuisine will be chosen by Claudio"
    elif cuisine_selection == "dennelise":
        text_cuisine = ", the cuisine will be chosen by Dennelise"
    else:
        text_cuisine = ", the cuisine will be " + cuisine_selection

    return text_cuisine, cuisine_selection

# Function that randomly selects if it's a new or repeated restaurant

def new_or_repeated():
    selecting_new_or_repeated = random.choice(new_repeated)

    text_new_or_repeated = ""

    if selecting_new_or_repeated == "New":
        text_new_or_repeated = " and it has to be a new restaurant."
    else:
        text_new_or_repeated = " and the restaurant can be repeated."

    return text_new_or_repeated, selecting_new_or_repeated

# These lines of code make available both variables returned in the functions
text_meal, meal_selection = meal_selector()
text_cuisine, cuisine_selection = cuisine_selector()
text_new_or_repeated, selecting_new_or_repeated = new_or_repeated()

text = text_meal + text_cuisine + text_new_or_repeated

# Function that will log each date

def history_logging():
    log = []

    today_date = date.today().strftime('%Y-%m-%d')

    log.insert(0, today_date)
    log.insert(1, meal_selection)
    log.insert(2, cuisine_selection)
    log.insert(3, selecting_new_or_repeated)

    return log

print(history_logging())



