from client_main import Catchat_Client

print("nickname?")
nickname = input("> ")

client = Catchat_Client(718, nickname)

input("Press enter to initialize_server on port 718")
client.initialize_server()

client.update_internal_list()

print("Type .2 to change nickname; .3 to send a DM; .4 to disconnect; .5 to exit")

while True:
    msg = input("> ")

    if msg == ".2":
        new_nick = input("New Nick > ")
        client.set_nickname(new_nick)

    elif msg == ".3":
        usrname = input("Type in username to whisper to > ")
        m = input("Enter your message > ")

        client.send_message(m, usrname)
    
    elif msg == ".4":
        client.disconnect()
    
    elif msg == ".5":
        quit()

    else:
        client.send_message(msg)

    