message = ["hi","bye","whats up"]

sent_messages = []

def send_messages():
  
    while message:
        msg = message.pop()
        print(message)
        sent_messages.append(msg)
        print(sent_messages)
  

send_messages()

['hi', 'bye']
['whats up']
['hi']
['whats up', 'bye']
[]
['whats up', 'bye', 'hi']