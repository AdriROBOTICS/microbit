from microbit import *
import radio

# Initialize radio and set group
radio.on()
radio.set_group(1) # Set a radio group (can be any number from 0-255)

while True:
    # Receive data from radio
    # Use radio.receive() to get the received data
    incoming = radio.receive()

    if incoming is not None:
        try:
            # Convert the received data to an integer
            steps_per_second = int(incoming)
            # Write the integer to the serial port
            print(steps_per_second)
        except ValueError:
            # Handle cases where the received data is not a valid integer
            display.show("!") # Indicate an error on the microbit display
            print("Invalid data received:", incoming)

    # Small delay to avoid busy waiting
    sleep(100)