import zmq
import time
import pandas as pd

file_path = 'file path'

def main():
    # Create a new context
    context = zmq.Context()

    # Create a publisher socket
    socket = context.socket(zmq.PUB)

    # Bind the socket to port 7786
    socket.bind("tcp://*:7786")

    print("Publisher started on port 7786")

    # Read and sort the CSV file by timestamp
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Ensure the timestamp column is in datetime format
    df.sort_values(by='timestamp', inplace=True)

    # Initialize variables
    previous_timestamp = None
    accumulated_lines = []

    # Iterate over the DataFrame rows
    for index, row in df.iterrows():
        current_timestamp = row['timestamp']
        row_data = row.to_frame().T.to_csv(index=False, header=False)

        if previous_timestamp is not None and current_timestamp != previous_timestamp:
            # Send accumulated lines
            message = ''.join(accumulated_lines)
            socket.send_string(message)
            print(f"Sent at {previous_timestamp}:\n{message}")
            accumulated_lines = []
            time.sleep(2)  # Sleep for 2 seconds

        # Accumulate lines with the same timestamp
        accumulated_lines.append(row_data)
        previous_timestamp = current_timestamp

    # Send any remaining accumulated lines
    if accumulated_lines:
        message = ''.join(accumulated_lines)
        socket.send_string(message)
        print(f"Sent at {previous_timestamp}:\n{message}")

if __name__ == "__main__":
    main()
