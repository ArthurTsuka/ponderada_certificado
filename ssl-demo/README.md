# SSL/TLS Demo - Tutorial Completo

Este projeto demonstra como implementar comunicação segura usando SSL/TLS com certificados autoassinados, seguindo o tutorial fornecido.

## 📋 Estrutura do Projeto

```
ssl-demo/
├── certificate.crt      # Certificado público autoassinado
├── private.key         # Chave privada
├── server.js           # Servidor HTTPS em Node.js
├── server.py           # Servidor HTTPS em Python/Flask
├── client.js           # Cliente HTTPS em Node.js
├── client.py           # Cliente HTTPS em Python
├── test_connection.sh  # Scripts de teste com curl/openssl
├── requirements.txt    # Dependências Python
└── README.md          # Esta documentação
```

## 🔐 1. Geração de Certificados (Já Executado)

Os certificados autoassinados já foram gerados usando:

```bash
openssl req -x509 -newkey rsa:2048 -keyout private.key -out certificate.crt -days 365 -nodes -subj "/C=BR/ST=SP/L=SaoPaulo/O=SSL-Demo/CN=localhost"
```

Isso criou:
- `certificate.crt`: Certificado público
- `private.key`: Chave privada

## 🚀 2. Como Executar

### Pré-requisitos

#### Para Node.js:
- Node.js instalado
- Nenhuma dependência adicional (usa módulos nativos)

#### Para Python:
- Python 3.7+
- Instalar dependências:
```bash
pip install -r requirements.txt
```

### Executando os Servidores

#### Servidor Node.js (Porta 8443)
```bash
node server.js
```

#### Servidor Flask (Porta 8444) 
```bash
python server.py
```

### Executando os Clientes

#### Cliente Node.js
```bash
node client.js
```

#### Cliente Python
```bash
python client.py
```

### Testes com Ferramentas de Sistema

#### Executar todos os testes automatizados:
```bash
chmod +x test_connection.sh
./test_connection.sh
```

#### Testes manuais com curl:
```bash
# GET request
curl -v -k https://localhost:8443

# POST request
curl -v -k -X POST \
  -H "Content-Type: application/json" \
  -d '{"msg":"Secret data that should be protected!"}' \
  https://localhost:8443/api/data
```

#### Testes com OpenSSL:
```bash
# Testar conexão
openssl s_client -connect localhost:8443 -servername localhost

# Verificar certificado
openssl x509 -in certificate.crt -text -noout
```

## 🧪 3. Cenários de Teste

### Servidor Node.js (Porta 8443)
- **GET /**: Retorna mensagem de conexão segura
- **POST /api/data**: Aceita JSON e retorna dados com flag de encriptação

### Servidor Flask (Porta 8444)
- **GET /**: Retorna mensagem de conexão segura
- **POST /api/data**: Aceita JSON e retorna dados com flag de encriptação

### Clientes
- Testam tanto GET quanto POST requests
- Demonstram como lidar com certificados autoassinados
- Mostram diferentes abordagens (Node.js nativo vs Python requests)

## ⚠️ 4. Configurações de Segurança

### Para Desenvolvimento (Atual)
- `rejectUnauthorized: false` (Node.js)
- `verify=False` (Python requests)
- `-k` flag (curl)

### Para Produção (Recomendado)
- Use certificados assinados por CA confiável
- Configure validação completa de certificados
- Use `verify='ca-bundle.crt'` ou similar

## 📊 5. Saída Esperada

### Cliente Executado com Sucesso:
```
--- Testing HTTPS GET Request ---
Status Code: 200
Response Body: Secure Connection Established via HTTPS!

--- Testing HTTPS POST Request ---
Status Code: 200
Response Body: {"received":{"msg":"Secret data that should be protected!"},"encrypted":true}
```

### Servidor Mostrando Requisições:
```
HTTPS Server received request from: ::1
Method: POST
URL: /api/data
HTTPS Server received: { msg: 'Secret data that should be protected!' }
```

## 🔧 6. Troubleshooting

### Erro de Porta em Uso
```bash
# Verificar processos usando as portas
lsof -i :8443
lsof -i :8444

# Encerrar processos se necessário
kill -9 <PID>
```

### Problemas com Certificados
```bash
# Verificar se os arquivos existem
ls -la certificate.crt private.key

# Verificar conteúdo do certificado
openssl x509 -in certificate.crt -text -noout
```

### Erro de Permissões (macOS/Linux)
```bash
# Dar permissão de execução ao script de teste
chmod +x test_connection.sh
```

## 📚 7. Explicação Técnica

### Diferenças entre HTTP e HTTPS
- **HTTP**: Dados transmitidos em texto claro
- **HTTPS**: Dados criptografados usando TLS/SSL

### Certificados Autoassinados
- ✅ **Vantagens**: Fácil de gerar, gratuito, criptografia funcional
- ❌ **Desvantagens**: Não confiável por padrão, warnings de segurança

### Fluxo de Comunicação Segura
1. Cliente inicia conexão TLS
2. Servidor apresenta certificado
3. Cliente verifica certificado (ou ignora se configurado)
4. Estabelecimento de chave de sessão
5. Dados criptografados são transmitidos

## 🎯 8. Próximos Passos

Para uso em produção, considere:
1. Obter certificados de CA confiável (Let's Encrypt, etc.)
2. Implementar renovação automática de certificados
3. Configurar HSTS headers
4. Implementar certificate pinning
5. Usar TLS 1.3 quando possível

## 📋 9. Comandos Úteis de Referência

```bash
# Gerar novo certificado
openssl req -x509 -newkey rsa:2048 -keyout private.key -out certificate.crt -days 365 -nodes

# Ver informações do certificado
openssl x509 -in certificate.crt -text -noout

# Testar conexão SSL
openssl s_client -connect localhost:8443

# Curl ignorando certificado
curl -k https://localhost:8443

# Verificar portas abertas
netstat -tulpn | grep :8443
```

---

**Nota**: Este projeto é para fins educacionais e desenvolvimento. Para uso em produção, sempre use certificados assinados por autoridades certificadoras confiáveis! 