from email import message


def send_messages(messages):
    send_messages=[]
    for message in messages:
        print(f'\n{message}')

    while messages:
        msg = messages.pop()
        print(f"los mensajes son:{msg}")
        send_messages.append(msg)


    print("\Los Mensajes a la nueva lista son:")
    for send_messagess in send_messages:
        print(send_messagess)


send_messages(['mensaje 1','mensaje 2','mensaje 3','mensaje 4'])   
print("=================")
send_messages




