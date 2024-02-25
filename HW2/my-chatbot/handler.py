import datetime
import requests
import random

# Function to invoke figlet with provided text
def invoke_figlet(text):
    figlet_response = requests.post("http://10.62.0.5:8080/function/figlet", data=text)
    if figlet_response.status_code == 200:
        return figlet_response.text
    else:
        return "Error invoking figlet function."

def handle(req):
    # Convert the input string to lowercase for case-insensitive matching
    input_data = req.lower()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if 'figlet for name' in input_data:
        return invoke_figlet("name")
    elif 'figlet for date' in input_data:
        return invoke_figlet("date")
    elif 'figlet for time' in input_data:
        return invoke_figlet("time")
    elif 'name' in input_data:
        names = ["ChatBot", "Bot", "Chatty"]
        return random.choice(["My name is {}.".format(names[0]), 
                              "You can call me {}.".format(names[1]), 
                              "I go by the name {}.".format(names[2])])
    elif 'date' in input_data:
        return random.choice(["The current date and time is {}.".format(current_time),
                              "It's currently {}.".format(current_time),
                              "The date right now is {}.".format(current_time)])
    elif 'time' in input_data:
        return random.choice(["The current date and time is {}.".format(current_time),
                              "It's currently {}.".format(current_time),
                              "The time right now is {}.".format(current_time)])
    elif 'figlet' in input_data:
        start_index = input_data.find("for ")
        if start_index != -1:
            figlet_text = input_data[start_index + 4:].strip()
            if figlet_text:
                return invoke_figlet(figlet_text)
            else:
                return "Please provide text for the figlet."
        else:
            return "Please provide text for the figlet."
    else:
        return "Sorry, I didn't understand the question."
