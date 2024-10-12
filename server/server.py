from flask import Flask, request, jsonify
import time
import json
from datetime import datetime
import socket

app = Flask(__name__)

port = 5000

def get_server_info():
    global port
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print("="*30)
    print(" Server Information ".center(30, "="))
    print(f"IP Address: {ip_address}")
    print(f"Port: {port}")
    print("="*30)

get_server_info()

def get_saved_messages(date):
    formatted_date = datetime.fromtimestamp(date)
    formatted_date = formatted_date.strftime("%Y-%m-%d")

    with open(f'messages/{formatted_date}.json', 'r') as f:
        data = json.load(f)

    return data

def add_message(author, message):
    formatted_date = time.strftime("%Y-%m-%d", time.localtime())
    timestamp = time.time()

    file_path = f'messages/{formatted_date}.json'
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"messages": []}

    data["messages"].append({
        "author": author,
        "message": message,
        "timestamp": timestamp
    })

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def credits():
    json_response = {"name": "EscapedShadows", "url": "actuallysecurechatapp.escapedshadows.com"}
    return jsonify(json_response)

@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.json
    print(data)

    author = data["author"]
    message = data["message"]

    add_message(author, message)

    return jsonify({"message": "success"}), 201

@app.route('/getMessages', methods=['POST'])
def get_messages():
    data = request.json
    date = data["date"]

    messages = get_saved_messages(date)

    return jsonify(messages)

app.run(host="0.0.0.0", debug=True, port=port)