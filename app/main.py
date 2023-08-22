# Uncomment this to pass the first stage
import socket
import re
import threading
from app.storageengine import QueryEngine

HAS_CR_LF = re.compile(r"[\r\n]+")
SIMPLE_STR = re.compile(r"^\+(.*)[\r\n|\n]$")
# SIMPLE_STR = re.compile(r"^\+(.*)\n")
BULK_STR = re.compile(r"^\$\d+\r\n(.*)\r\n$")

SnapshotFilePath = "./data/data.json"
QueryEngineInstance = QueryEngine("localhost", 6379)
QueryEngineInstance.SetSnapshotFilePath(SnapshotFilePath)
QueryEngineInstance.LoadDataInFile()


def serialize_simple_string(s: str) -> str:
    if HAS_CR_LF.search(s):
        raise Exception("Cannot serialize string containing \r or \n as simple string")
    return f"+{s}\n"


def deserialize_simple_string(s: str) -> str:
    return SIMPLE_STR.match(s).group(1)


def is_simple_string(s: str) -> bool:
    return SIMPLE_STR.match(s) is not None


def handle_connection(client , addr):
    with client: 
        while True:
            raw_request = client.recv(1024)
            if not raw_request:
                break
            decoded_raw_request = raw_request.decode("utf-8")
            isValid = is_simple_string(decoded_raw_request)
            if(isValid):
                print("data : " , raw_request)
                deserialize_raw_request= deserialize_simple_string(decoded_raw_request)
                print(deserialize_raw_request)
                raw_response = QueryEngineInstance.query(deserialize_raw_request)
                serialize_raw_response = serialize_simple_string(raw_response)
                client.sendall(serialize_raw_response.encode("utf-8"))





         



def main():
    print("Logs from your program will appear here!")
    # start redis server
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True : 
        conn, addr = server_socket.accept()  # wait for client
        print(f"Connected by {addr}")
        # make new thread to handle this client
        threading.Thread(target=handle_connection, args=(conn,addr)).start()
       

if __name__ == "__main__":
    main()
