# Import the random module
import random

# Define variables 
name = "Nidhi"   
weather = "cloudy"
flag=1

# Define a dictionary containing a list of responses for each message
#str.formate(str) used for substituting 
responses = {
  "what is your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "what is your hobby?":[
      "I love to play Gitar",
      "I like reading books",
      "I love nightouts"
  ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    return bot_message
while(flag):
    question=input("write your question......or write Q to Quit....")
    if question=="Q":
        flag=0
    else:
        print(respond(question))
    
