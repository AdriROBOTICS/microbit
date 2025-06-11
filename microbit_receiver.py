from microbit import *
import radio
paso = 0
steps = 0
# Initialize radio and set group
radio.on()
radio.set_group(24) # Set a radio group (can be any number from 0-255)
def on_received_number(incoming):
    global steps
    if incoming is not None:
                try:
                    # Convert the received data to an integer
                    steps = incoming
                    # Write the integer to the serial port
                    print(steps)
                except:
                    # Handle cases where the received data is not a valid integer
                    basic.show_icon(IconNames.DUCK)
                     # Indicate an error on the microbit display
                    basic.show_string(f"Invalid data received")
    basic.pause(100)

while True:
    if input.button_is_pressed(Button.A):
        paso += 1
        print(paso)
    