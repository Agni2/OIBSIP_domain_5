# OIBSIP_domain_5

# 🗨️ Chat Bot 
This is a basic terminal-based chat application built using Python’s socket and threading modules. It allows multiple clients to connect to a server and exchange real-time messages in a shared chatroom.

## 📌 Objective
To build a lightweight, text-based chatroom using Python sockets that demonstrates the fundamentals of network programming, threading, and client-server architecture.

## 🚀 How It Works
Server (server.py)
Listens for incoming client connections.

Manages connected clients using threads.

Handles broadcasting of messages to all active users.

Responds to nickname requests from clients.

Client (client.py)
Connects to the server using socket.

Sends and receives messages.

Each client chooses a nickname.

Runs two threads: one for sending messages, one for receiving.

## 🧰 Tools & Technologies Used
Python 3

socket – for network communication

threading – to handle concurrent clients and continuous read/write loops

