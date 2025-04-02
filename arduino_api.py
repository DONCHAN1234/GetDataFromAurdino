import streamlit as st
import serial  # Import pyserial
import time

# Replace 'COM3' with your Arduino's port (e.g., '/dev/ttyUSB0' on Mac/Linux)
arduino_port = "COM5"  
baud_rate = 9600  # Must match the baud rate in the Arduino code

try:
    # Establish serial communication
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    st.write(f"Connected to Arduino on {arduino_port}")
except serial.SerialException as e:
    st.write(f"Error: Could not connect to Arduino - {e}")
    st.stop()

# Create a placeholder in Streamlit for displaying data
placeholder = st.empty()

while True:
    try:
        # Read a line of data from the Arduino
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').strip()  # Decode and clean data
            placeholder.write(f"Received data: {data}")
    except Exception as e:
        placeholder.write(f"Error reading data: {e}")

    time.sleep(1)  # Update every second
