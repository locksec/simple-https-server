# Author: Ray Heffer
# Website: https://www.rayheffer.com
# Date Created: October 16, 2023
# Description: Simple HTTPS Server with mTLS

import http.server
import ssl
import argparse
import socket

# Get local IP address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Makes connection to 1.1.1.1 to find local machine IP (E.g. 192.168.10.200)
        s.connect(('1.1.1.1', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        # Fallback to localhost IP if external IP detection fails
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

# HTTPS Server, gets parsed arguments
def run_server(port, certfile, keyfile, cafile, listen_ip):
    local_ip = listen_ip or get_local_ip()
    
    # Initialize server listening on all interfaces
    server_address = (local_ip, port)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    
    # Wrap the HTTP server socket with SSL
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   certfile=certfile,
                                   keyfile=keyfile,
                                   cert_reqs=ssl.CERT_REQUIRED,
                                   ca_certs=cafile)

    print(f"Server running on: https://{local_ip}:{port}/")
    httpd.serve_forever()

# Main function to parse command line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Start a simple HTTPS server with mTLS.')
    parser.add_argument('-p', '--port', type=int, required=True, help='The port to listen on.')
    parser.add_argument('-c', '--certfile', type=str, required=True, help='Server certificate file.')
    parser.add_argument('-k', '--keyfile', type=str, required=True, help='Server private key file.')
    parser.add_argument('-a', '--cafile', type=str, required=True, help='CA certificate file for client verification.')
    parser.add_argument('-l', '--listen', type=str, default='127.0.0.1', help='IP address to listen on. Defaults to 127.0.0.1.')

    args = parser.parse_args()
    run_server(args.port, args.certfile, args.keyfile, args.cafile, args.listen)
