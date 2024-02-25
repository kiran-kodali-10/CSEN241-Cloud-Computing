import requests
import time

# Function to send a request to the chatbot function and measure response time
def send_request(input_data):
    start_time = time.time()
    response = requests.post("http://10.62.0.5:8080/function/my-chatbot", data=input_data)
    end_time = time.time()
    response_time = end_time - start_time
    return response, response_time

# Test Scenario 1: Response Time for the First Request that Does Not Call Figlet
input_data = "What is your name?"
response, response_time = send_request(input_data)
print("Test Scenario 1 - Response Time for the First Request that Does Not Call Figlet:")
print("Response:", response.text)
print("Response Time:", response_time, "seconds")
print()

# Test Scenario 2: Response Time for the Second Request that Does Not Call Figlet
input_data = "What time is it?"
response, response_time = send_request(input_data)
print("Test Scenario 2 - Response Time for the Second Request that Does Not Call Figlet:")
print("Response:", response.text)
print("Response Time:", response_time, "seconds")
print()

# Test Scenario 3: Average Response Time Over 10 Requests that Do Not Call Figlet
total_response_time = 0
for _ in range(10):
    input_data = "What is your name?"
    _, response_time = send_request(input_data)
    total_response_time += response_time
average_response_time = total_response_time / 10
print("Test Scenario 3 - Average Response Time Over 10 Requests that Do Not Call Figlet:")
print("Average Response Time:", average_response_time, "seconds")
print()

# Test Scenario 4: Response Time for the First Request that Calls Figlet
input_data = "figlet for hello"
response, response_time = send_request(input_data)
print("Test Scenario 4 - Response Time for the First Request that Calls Figlet:")
print("Response:", response.text)
print("Response Time:", response_time, "seconds")
print()

# Test Scenario 5: Response Time for the Second Request that Calls Figlet
input_data = "figlet for hello"
_, _ = send_request(input_data)  # First request to warm up the function
response, response_time = send_request(input_data)
print("Test Scenario 5 - Response Time for the Second Request that Calls Figlet:")
print("Response:", response.text)
print("Response Time:", response_time, "seconds")
print()

# Test Scenario 6: Response Time for the Second Request that Calls Figlet Following the First Request that Does Not Call Figlet
input_data = "What is your name?"  # First request that does not call figlet
_, _ = send_request(input_data)  # Warm up the function
input_data = "figlet for hello"  # Second request that calls figlet
response, response_time = send_request(input_data)
print("Test Scenario 6 - Response Time for the Second Request that Calls Figlet Following the First Request that Does Not Call Figlet:")
print("Response:", response.text)
print("Response Time:", response_time, "seconds")
print()

# Test Scenario 7: Average Response Time Over 10 Requests that Call Figlet
total_response_time = 0
for _ in range(10):
    input_data = "figlet for hello"
    _, response_time = send_request(input_data)
    total_response_time += response_time
average_response_time = total_response_time / 10
print("Test Scenario 7 - Average Response Time Over 10 Requests that Call Figlet:")
print("Average Response Time:", average_response_time, "seconds")
