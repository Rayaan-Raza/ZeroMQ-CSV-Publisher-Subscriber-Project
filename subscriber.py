import zmq

def main():
    # Create a new context
    context = zmq.Context()

    # Create a subscriber socket
    socket = context.socket(zmq.SUB)

    # Connect the socket to the publisher's address and port
    socket.connect("tcp://localhost:7786")

    # Subscribe to all messages
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    print("Subscriber connected to port 7786")

    # Receive messages
    while True:
        message = socket.recv_string()
        print(f"Received: {message}")

if __name__ == "__main__":
    main()
