from flask import Flask, jsonify
import serial

app = Flask(__name__)

def get_arduino_data():
    ser = serial.Serial('COM5', 9600)  
    if ser :
        print('Data 1 fetched')
    line = ser.readline().decode('utf-8').strip()
    if line :
        print(line)
    return line

@app.route('/get_data', methods=['GET'])
def get_data():
    data = get_arduino_data()
    return jsonify({"data": data})

if __name__ == "__main__":
    app.run(debug=True)
