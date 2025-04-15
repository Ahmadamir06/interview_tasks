# using flask, have not built a webapp in a sec so this is annoyingly slow to get set up
# need to set up get and post enpoints for the chat messages and then preferrably make it look good
# one way to make it look nice and work real time would be to use react, but i have not used react with python & flask
# could switch to js but at this point i have wasted enough time
 
#ok i have a working handler, i just need to set up the post handler to call the llm_call function and store and show the messages to the user
# i have to remeber to write down the usage instructions and add .env to the .gitignore file
# having problems with the flask/django html form not working so ill just have leave that out
# 5 minutes left now, so ill finish up

#get requirements from requirements.txt
# use flask --app webapp run 
# only post available due to time constraints
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")

def llm_call(message: str):
    client = OpenAI()

    response = client.responses.create(
        model="gpt-4.1",
        input= message
    )

    return response.output_text
    
print(llm_call("hello ai"))
