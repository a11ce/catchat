'''
Client uses a queue for tracking status of messages

'''


class Catchat_Client:
    def __init__(self, port, nickname):
        self.port = port

        self.nickname = nickname

        self.people = []

        # Message queue stores triples of (msgID, header, msg)
        self.message_queue = []

        self.topID = 0

        self.connected = False
        self.verified_new_nick = False

    def transmit(self, command_id, msg=""):
        msg = command_id + " " + msg

        print("TRANSMITTED: ", msg)

        self.message_queue.insert(0, (self.get_msgID(), "NICK", msg))

    def initialize_server(self):
        # More stuff needed for actual networking

        self.transmit("HELO", self.nickname)

    def disconnect(self, reason=""):
        msg = f"{reason}"
        self.transmit("CYOU", msg)

    def get_msgID(self):
        self.topID += 1
        return self.topID

    def process_data(self, message):
        # Returns 1 if successful parsing

        command_id = message[:4]

        msg = message[4:]

        if command_id == "DONE":
            verified_msg = message_queue.pop()

            if verified_msg[1] == "HELO":
                self.verified_new_nick = True
                self.connected = True

            elif verified_msg[1] == "NICK":
                self.verified_new_nick = True

            elif verified_msg[1] == "CYOU":
                self.connected = False
                # Other networking stuff may be needed?

            elif verified_msg[1] == "SEND":
                pass
                # Further stuff needed to allow messge status to be parsed

            elif verified_msg[1] == "LIST":
                self.list = [x.split(' ') for x in msg.split(', ')] 

            return 1

        elif command_id == "EROR":
            return

        elif command_id == "NEWU":
            return

        elif command_id == "NICK":
            return

        elif command_id == "CYOU":
            return

        elif command_id == "MESG":
            print("New message!", msg)

        else:
            print("BAD INCOMMING MESSAGE!!!! THAT'S INVALID | ", message)

    def set_nickname(self, new_nick):
        self.nickname = new_nick

        self.transmit("NICK", new_nick)
        self.verified_new_nick = False

    def send_message(self, msg, to_usr=None):
        if to_usr:
            body = f"{to_usr} {msg}"
        else:
            body = f"* {msg}"

        self.transmit("SEND", body)

    def update_internal_list(self):
        self.transmit("LIST")


if __name__ == '__main__':
    client = Catchat_Client(100, "Jackson")

    client.initialize_server()

    client.set_nickname("FIFO")

    client.send_message("Hello World")
    client.send_message("Hello World", "HAL9000")

    client.update_internal_list()

    client.disconnect()


