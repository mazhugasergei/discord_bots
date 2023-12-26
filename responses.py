import random

options = {
  "hello": "Hi there!"
}

def handle_response(message: str) -> str:
  if message[0] == "!":
    message = message[1:]
  else:
    return
  
  message = message.lower()

  if message in options:
    return options[message]