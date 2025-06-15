import requests
import json
import urllib3

# Desabilita warning de certificados não verificados (apenas para desenvolvimento)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_nodejs_server():
    print("--- Testing Node.js HTTPS Server (port 8443) ---")
    
    try:
        # GET Request
        print("\n1. Testing GET Request:")
        response = requests.get(
            'https://localhost:8443',
            verify=False  # Para certificados autoassinados (não recomendado em produção)
            # verify='certificate.crt'  # Alternativa: especificar o certificado
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        # POST Request
        print("\n2. Testing POST Request:")
        data = {'msg': 'Secret data that should be protected!'}
        response = requests.post(
            'https://localhost:8443/api/data',
            json=data,
            verify=False
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Node.js server: {e}")
        print("Make sure the Node.js server is running: node server.js")

def test_flask_server():
    print("\n--- Testing Flask HTTPS Server (port 8444) ---")
    
    try:
        # GET Request
        print("\n1. Testing GET Request:")
        response = requests.get(
            'https://localhost:8444',
            verify=False
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        # POST Request
        print("\n2. Testing POST Request:")
        data = {'msg': 'Secret data that should be protected!'}
        response = requests.post(
            'https://localhost:8444/api/data',
            json=data,
            verify=False
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Flask server: {e}")
        print("Make sure the Flask server is running: python server.py")

if __name__ == '__main__':
    print("Starting HTTPS Client Tests...")
    print("Testing both Node.js and Flask servers\n")
    
    test_nodejs_server()
    test_flask_server()
    
    print("\n" + "="*50)
    print("HTTPS Client Tests Completed!")
    print("Note: Using verify=False for self-signed certificates")
    print("In production, use proper CA-signed certificates") 