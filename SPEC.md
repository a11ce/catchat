- All interactions between client and server are plaintext
- A command consists of a command ID and then associated data
- The recipient of a command always responds, either with `DONE` if successful (and the requested data if applicable) or `ERR` (with information) if not
- Nicknames must be alphanumeric

### Commands

#### Client to server
- All commands can trigger a `EROR SAYHI` response if the user hasn't registered a nickname.
- `HELO <nickname>` registers connection to the server with the given nickname.
    - `DONE` if registered.
    - `EROR BADNAME` if unsuitable username.
    - `EROR TAKEN` if name is already taken
- `NICK <nickname>` changes the user's registered nickname.
    - Same as above.
- `BYE [reason]` disconnects, optionally with a reason.
    - `EROR NOTSENT` if the disconnect message could not be sent.
    - `DONE` if the disconnect message was sent (this response probably doesn't matter).
- `MESG <nickname|*> <message>` sends a message to a certain person or to everyone connected.
    - `EROR NOUSER` if the given nickname is not online.
    - `EROR NOTSENT` if the message could not be sent.
    - `DONE` otherwise.
- `LIST` gets info about currently connected users.
    - `DONE <user <ip|hostname>> [, <...]`
    
#### Server to client
- `NEW <nickname> <ip|hostname>` notifies of a newly joined user.
    - `DONE` when received.
- `NICK <old> <new>` notifies of a changed nickname.
    - `DONE` when received.
- `BYE <nickname> <DISC|LOST|reason>` notifies that a user has left, distinguishing between a disconnect with no message and a lost connection.
    - `DONE` when received.
- `MESG <PRIV|*> <nickname> <message>` notifies of a received message, either private or public, and who it was from.
    - `DONE` when received.
