# torIPchanger
To enable the control port for changing the IP address via the console on Linux, you can follow these steps:

Open the Tor configuration file using a text editor. The location of the file may vary depending on your distribution, but it is generally located at /etc/tor/torrc.

Uncomment the following line by removing the '#' symbol, if it exists:
```
#ControlPort 9051
```

It should now look like this:
```
ControlPort 9051
```

This line sets the port that Tor uses for control connections.

Optionally, you can also set a password to restrict access to the control port. Uncomment the following line, remove the '#' symbol, and specify your desired password:
```
#HashedControlPassword <password>
```
Note that <password> should be replaced with the actual hashed password. You can generate the hashed password by running the command tor --hash-password <your_password> in the terminal. Replace <your_password> with your desired password.

Save the changes and exit the text editor.

Restart the Tor service for the changes to take effect. The command to do this may vary depending on your Linux distribution, but it is usually one of the following:
```
sudo systemctl restart tor
```
or
```
sudo service tor restart
```
Now, you can use the control port to change the IP address via the console by sending commands to the Tor control port using the Tor Control Protocol (TCP). For example, you can use telnet or nc commands to connect to the control port and issue commands. Here's an example using telnet:
```
telnet localhost 9051
```
After establishing the connection, you can send commands such as SIGNAL NEWNYM to request a new IP address.
