
# ZeroMQ CSV Publisher-Subscriber Project

This project demonstrates a simple publish-subscribe messaging pattern using ZeroMQ. The publisher reads a CSV file, sorts the data by timestamp, and sends messages periodically. The subscriber listens for these messages and prints them.

## Features

- **Publisher**: Reads a CSV file, sorts it by timestamp, and sends messages every 2 seconds.
- **Subscriber**: Listens for messages from the publisher and prints the received data.
- **ZeroMQ**: Utilizes ZeroMQ for efficient message passing.

## Prerequisites

- Python 3.x
- `pandas` library
- `pyzmq` library

You can install the required libraries using pip:

```bash
pip install pandas pyzmq
