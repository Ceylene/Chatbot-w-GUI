import random
import json


with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

bot_name = "Ceylene"

def get_response(msg):
  # print("Let's chat! (type 'quit' to exit)")
  # user_name = input("What's your name? ")
  # print(f"Hi {user_name}!")
  while True:
    sentence = input("You: ").lower()
    if sentence == "quit":
        break
    if len(sentence) < 10000:
      for intent in intents['intents']:
        if sentence in intent["words"]:
        # for word in sentence.split(" "):
        #   if word == intent["tag"]:
          return random.choice(intent['responses'])