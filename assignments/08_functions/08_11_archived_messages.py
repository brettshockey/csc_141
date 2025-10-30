message = ["Yo","bye","whats up"]
sent_messages = []

def send_messages(message):
  
    while message:
        msg = message.pop()
        print(message)
        sent_messages.append(msg)
        print(sent_messages)
  

send_messages(message[:])
print(message)