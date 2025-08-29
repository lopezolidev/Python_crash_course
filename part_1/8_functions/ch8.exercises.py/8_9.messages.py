messages = [
    "hello",
    "hi there",
    "sup'",
    "howdy"
]

def message_printing(msgs):
    while msgs:
        current_message = msgs.pop()
        print(f"Your text message says: {current_message}")


message_printing(messages)