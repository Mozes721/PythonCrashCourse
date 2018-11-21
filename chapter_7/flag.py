prompt = "\n Tell me where u live"
prompt += "\n Enter 'quit' to end the program "



while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print("Id love to visit you at " + message.title())
