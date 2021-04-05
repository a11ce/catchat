- All interactions between client and server are plaintext
- A command consists of a command ID and then associated data
- The recipient of a command always responds, either with `DONE` if successful (and the requested data if applicable) or `ERR` (with information) if not
- Nicknames must be alphanumeric

### Commands

#### Client to server
- `HELO <nickname>` registers connection to the server with the given nickname.
- `NICK <nickname>` changes the user's registered nickname.
- `BYE [reason]` disconnects, optionally with a reason.
- `MESG <nickname|*> <message>` sends a message to a certain person or to everyone connected. 
- `LIST` gets info about currently connected users.

#### Server to client
- `NEW <nickname> <ip|hostname>` notifies of a newly joined user.
- `NICK <old> <new>` notifies of a changed nickname.
- `BYE <nickname> <DISC|LOST|reason>` notifies that a user has left, distinguishing between a disconnect with no message and a lost connection.
- `MESG <PRIV|*> <nickname> <message>` notifies of a received message, either private or public, and who it was from.
