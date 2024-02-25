import datetime
import requests
import random

# Function to call the figlet service with the given text
def call_figlet_service(text):
    figlet_response = requests.post("http://10.62.0.5:8080/function/figlet", data=text)
    if figlet_response.status_code == 200:
        return figlet_response.text
    else:
        return "Error calling the figlet service."

def process_request(req):
    # Convert the input string to lowercase for case-insensitive matching
    input_data = req.lower()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if 'figlet for name' in input_data:
        return call_figlet_service("name")
    elif 'figlet for date' in input_data:
        return call_figlet_service("date")
    elif 'figlet for time' in input_data:
        return call_figlet_service("time")
    elif 'name' in input_data:
        names = ["ChatBot", "Bot", "Chatty"]
        return random.choice(["My name is {}.".format(names[0]),
                              "You can refer to me as {}.".format(names[1]),
                              "I respond to the name {}.".format(names[2])])
    elif 'date' in input_data or 'time' in input_data:
        return random.choice(["The current date and time is {}.".format(current_time),
                              "It's presently {}.".format(current_time),
                              "The date and time right now are {}.".format(current_time)])
    elif 'figlet' in input_data:
        start_index = input_data.find("for ")
        if start_index != -1:
            figlet_text = input_data[start_index + 4:].strip()
            if figlet_text:
                return call_figlet_service(figlet_text)
            else:
                return "Please provide text for the figlet."
        else:
            return "Please provide text for the figlet."
    else:
        return "Apologies, I couldn't comprehend the request."
