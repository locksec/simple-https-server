# Simple HTTPS Server with mTLS
A Python-based HTTPS server that supports Mutual TLS (mTLS). This simple server can be used for a variety of applications, such as Vault PKI demonstrations, running a secure internal web service, or for ethical hacking practices for certifications like OSCP or CEH.

## Prerequisites
- Python 3.x
- OpenSSL (For generating certificates and keys)

## Features
- Supports HTTPS using TLS
- Supports mTLS for client verification
- Customizable IP and port
- Utilizes Python's `http.server` and `ssl` modules

## Usage
To run the server, execute the following command:
```bash
python3 server.py -p 8443 -l 0.0.0.0 -c server.crt -k server.key -a ca.crt
```
**Note**: If no listener IP is specified, it will default to 127.0.0.1.

To test the server using curl, execute the following command:
``` bash
curl -k --cert client.crt --key client.key https://127.0.0.1:8443
```
## Switches
* `-p`, `--port`: The port to listen on. E.g. 8443
* `-l`, `--listen`: The IP address to listen on (defaults to 127.0.0.1 if this is omitted). E.g. 0.0.0.0
* `-c`, `--certfile`: The server certificate file. This is the public certificate that the server presents during the handshake.
* `-k`, `--keyfile`: The server private key file. This private key corresponds to the public certificate specified in `--certfile`.
* `-a`, `--cafile`: The CA certificate file for client verification. This is the CA that signed the client's certificate.
* `-m`, `--mtls`: Enables mTLS, which will require the client to provide a valid certificate.

## Examples of Use Cases
* Vault PKI Demo: You can use this server to demonstrate how Vault can issue certificates. Use the CA certificate from Vault as `ca.crt`, and Vault-issued certificates as `server.crt` and `server.key`.
* Ethical Hacking: This setup can be used to practice mTLS and SSL exploitation techniques in a controlled environment. Useful for certifications like OSCP or CEH.
* Secure Internal Web Services: Use this as a simple HTTPS server with client verification for running secure internal web services.