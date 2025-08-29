messages = [
    "hello",
    "hi there",
    "sup'",
    "howdy"
]

sent_messages = []

def message_printing(msgs, sent):
    while msgs:
        current_message = msgs.pop()
        print(f"Your text message says: {current_message}")
        sent.append(current_message)

message_printing(messages[:], sent=sent_messages)
# calling the function with a copy of the list of messages

print(f"\nList of messages: {messages}")
print(f"List of sent messages: {sent_messages}")
# List of messages: ['hello', 'hi there', "sup'", 'howdy']
# List of sent messages: ['howdy', "sup'", 'hi there', 'hello']