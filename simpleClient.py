import time
import requests
from client.AESCipher import AESCipher

Cipher = AESCipher("7ace600265104e1c1054cb25d0aee8d02678741e7bf2b4701df61f1d32a716863bffd67c5c4e978e0df898ec2820e20226cbb888bbb98d317a206ecf6f15ccb6")

def send_message(data):
    response = requests.post(url="http://192.168.2.128:5000/sendMessage", json=data)
    return response.json()

def get_messages(date):
    decrypted_data = {"messages": []}
    data = {"date":date}
    response = requests.post(url="http://192.168.2.128:5000/getMessages", json=data)
    
    for message_data in response.json()["messages"]:
        author = message_data["author"]
        message = message_data["message"]
        timestamp = message_data["timestamp"]

        author = Cipher.decrypt(author)
        message = Cipher.decrypt(message)

        data = {
            "author": author,
            "message": message,
            "timestamp": timestamp
        }

        decrypted_data["messages"].append(data)
    
    return decrypted_data


author = "EscapedShadows"
message = "some important password"

encrypted_author = Cipher.encrypt(author)
encrypted_message = Cipher.encrypt(message)

data = {
    "author": encrypted_author,
    "message": encrypted_message
}

#send_message(data)
messages = get_messages(time.time())

print(messages)