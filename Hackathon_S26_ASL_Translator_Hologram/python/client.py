import http.client as client
import json
import time


msg = "TEST yguyguuygyugyugyuih"
connection = client.HTTPConnection('192.168.4.22', 80, timeout=10)
headers = {'Content-type': 'application/json'}


def convert_string(s):
    return  s.replace(' ', '%20')

def send(conn):
    conn.request('GET', f'/send?msg={convert_string(msg)}')
    print("Connection requested GET")
    response = conn.getresponse()
    print(f"Status: {response.status}")
    print(f"Response: {response.read().decode()}")


last_update_time = time.time()

while (True):
    try:
        if (time.time() - last_update_time > 1): 
            send(conn=connection)
            last_update_time = time.time()
    except KeyboardInterrupt as e:
        print(e)
        print("Program ended manually")
        break
    except Exception as e:
        print("Program encountered unexpected error")
        print(e)
        break

connection.close()
print("Connection closed")