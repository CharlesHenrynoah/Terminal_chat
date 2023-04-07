# -*- coding: utf-8 -*-
import socket
import threading


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))

    def send(self, message):
        self.client_socket.sendall(message.encode())

    def receive(self):
        return self.client_socket.recv(1024).decode()

    def disconnect(self):
        self.client_socket.close()
