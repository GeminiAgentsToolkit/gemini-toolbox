import vertexai
from gemini_toolbox import client

def get_current_time():
    """returns current time"""
    return "6pm PST"


def say_to_duck(say):
    """say something to a duck"""
    return f"duck answer is: duck duck {say} duck duck duck"

vertexai.init(project="gemini-trading-backend", location="us-west1")

all_functions = [get_current_time, say_to_duck]
clt = client.generate_chat_client_from_functions_list(all_functions, model_name="gemini-1.5-pro", debug=True, recreate_client_each_time=False, history_depth=3, add_scheduling_functions=True, gcs_bucket="gemini_jobs", gcs_blob="jobs.json")

# print(clt.send_message("say to the duck message: I am hungry"))
# print(clt.send_message("say to the duck message: I am hungry"))

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break
        response = clt.send_message(user_input)
        print("Jessica:", response)
