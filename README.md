This is a reverse shell I wrote from scratch to better understand how socket-based communication and remote command execution actually work. Tools like Metasploit can automate this, but I wanted to see how it works, so I learned how to build one.

The shell connects a server (attacker) to a client (target) using Python’s socket module. The server sends commands, the client executes them with subprocess, and the output is returned in real time. It also supports cd for changing directories, and the prompt updates to reflect the client’s current working directory.

This was built for educational purposes and currently runs locally. Future updates may include file transfer, authentication, and obfuscation features. If you're learning or teaching this kind of thing, feel free to explore or offer suggestions.
