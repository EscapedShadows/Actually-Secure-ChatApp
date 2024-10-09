# Actually Secure ChatApp
### A Project by [EscapedShadows](https://actuallysecurechatapp.escapedshadows.com)

## Overview

Actually Secure ChatApp is a secure chat application built with Python and Flask, designed for self-hosting. It prioritizes user privacy and offers a robust solution for private communications.

## Key Features

- **End-to-End Encryption**: All messages are encrypted on the client side before transmission, ensuring secure communication.
- **Fully Self-Hosted**: Enjoy total control and autonomy without reliance on external servers or databases.
- **Zero Data Collection**: Your privacy is respected; we do not collect any user data.

---

&nbsp;

# Setup Instructions

**Skip to Client Instructions if you do not want to set up your own server and already have one / received a key.**

&nbsp;

## Step 1: Install Required Packages

### You can install the required packages using pip:

```bash
pip install flask cryptography
```

## Step 2: Download the Code

### Download the latest `server.zip` release from the [GitHub repository](https://github.com/EscapedShadows/Actually-Secure-ChatApp/releases). Extract the ZIP file and navigate to the folder using your terminal or command prompt.

## Step 3: Generate a Secret Key

### Generate a secret key using the following command:

**For Windows:**

```bash
python keyGenerator.py
```

&nbsp;

**For Linux:**

```bash
python3 keyGenerator.py
```

### This will create a `secret.key` file containing your generated secret key.

## Step 4: Host the Server

### To host your ChatApp, you will need a server that supports Python and is accessible over the web. You can use any service that allows you to host your own cloud server. If you want to use the app locally, you can run it on your machine.

## Step 5: Upload `server.py`

### You will need to upload the `server.py` file to your server and run it. This will start the server and make it accessible over the web. Copy and paste the information printed when you start the server into a text editor.

## Step 6: Run `test.py`

### Replace `[your_ip]` in `test.py` with your server's IP address. Run the `test.py` file to test your ChatApp. You are ready to go!

&nbsp;
### 
&nbsp;

# Client Instructions

## Step 1: Get the Client

### Get the latest `client.zip` release from the [GitHub repository](https://github.com/EscapedShadows/Actually-Secure-ChatApp/releases). Extract the ZIP file and navigate to the folder using your terminal or command prompt.

### To set up your client, simply run:

**For Windows:**

```bash
python setup.py --ip [servers_ip] --key [secret_key]
```

&nbsp;

**For Linux:**

```bash
python3 setup.py --ip [servers_ip] --key [secret_key]
```

## Step 2: Decide on a Client

### There are two clients available:
- Terminal
- Web

### I think it's self-explanatory what the difference is. I recommend the Web Version, but hey, it's up to you!

### To choose the client, simply run the following command in your terminal:

**For Windows:**

```bash
python setup.py --client [terminal/web]
```

&nbsp;

**For Linux:**

```bash
python3 setup.py --client [terminal/web]
```

### Depending on your operating system, there will be a `.bat` or `.sh` file generated, allowing you to quickly start the application.

## Step 3: Finished!

### Alright, you are all set for the next level of private conversations! Have fun!

# Notes

- If you are having trouble with the setup, please refer to the [Troubleshooting Guide](https://actuallysecurechatapp.escapedshadows.com/troubleshooting).
- Please be kind to me; I don’t have much time to develop this project, but I hope someone out there will actually appreciate it. :)

# Development Plan

- [ ] Deleting Messages
- [ ] Sending Attachments (very limited size for now)
- [ ] Adding some sort of authentication system for the server so that only trusted clients can connect
- [ ] Error handling :D

### **A Project made with ❤️ by [EscapedShadows](https://escapedshadows.com)**
:red_heart: