#!/bin/bash

echo "========================================="
echo "          SSL/TLS Connection Tests"
echo "========================================="
echo ""

# Teste 1: Curl com Node.js server
echo "1. Testing with curl - Node.js Server (port 8443)"
echo "---------------------------------------------------"
echo "GET Request:"
curl -v -k https://localhost:8443
echo ""
echo ""

echo "POST Request:"
curl -v -k -X POST \
  -H "Content-Type: application/json" \
  -d '{"msg":"Secret data that should be protected!"}' \
  https://localhost:8443/api/data
echo ""
echo ""

# Teste 2: Curl com Flask server 
echo "2. Testing with curl - Flask Server (port 8444)"
echo "------------------------------------------------"
echo "GET Request:"
curl -v -k https://localhost:8444
echo ""
echo ""

echo "POST Request:"
curl -v -k -X POST \
  -H "Content-Type: application/json" \
  -d '{"msg":"Secret data that should be protected!"}' \
  https://localhost:8444/api/data
echo ""
echo ""

# Teste 3: OpenSSL connection test
echo "3. Testing with OpenSSL s_client"
echo "---------------------------------"
echo "Node.js Server (port 8443):"
echo "GET / HTTP/1.1" | openssl s_client -connect localhost:8443 -servername localhost -verify_return_error 2>/dev/null || echo "Connection test completed (self-signed certificate expected to fail verification)"
echo ""

echo "Flask Server (port 8444):"
echo "GET / HTTP/1.1" | openssl s_client -connect localhost:8444 -servername localhost -verify_return_error 2>/dev/null || echo "Connection test completed (self-signed certificate expected to fail verification)"
echo ""

# Teste 4: Verificar informações do certificado
echo "4. Certificate Information"
echo "--------------------------"
echo "Certificate details:"
openssl x509 -in certificate.crt -text -noout | head -20
echo ""

echo "Certificate fingerprint:"
openssl x509 -in certificate.crt -fingerprint -noout
echo ""

echo "========================================="
echo "           Tests Completed"
echo "========================================="
echo ""
echo "Notes:"
echo "- Using -k flag with curl to accept self-signed certificates"
echo "- In production, use proper CA-signed certificates"
echo "- Self-signed certificates will show verification errors (this is expected)" 