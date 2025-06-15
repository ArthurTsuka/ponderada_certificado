# Demonstração de Segurança SSL/TLS

Este projeto demonstra a implementação de comunicação segura entre um servidor Flask e um cliente Streamlit usando SSL/TLS.

## Estrutura do Projeto

- `server.py`: Servidor Flask com endpoints seguros
- `front.py`: Cliente Streamlit que se comunica com o servidor
- `certificate.crt`: Certificado SSL
- `private.key`: Chave privada
- `requirements.txt`: Dependências do projeto

## Passo 1: Gerar Certificados SSL

Para gerar os certificados SSL autoassinados, execute:

```bash
openssl req -x509 -newkey rsa:4096 -nodes -out certificate.crt -keyout private.key -days 365
```

## Passo 2: Instalar Dependências

```bash
pip install -r requirements.txt
```

## Passo 3: Executar o Servidor

```bash
python server.py
```

## Passo 4: Executar o Cliente

```bash
streamlit run front.py
```

## Como Funciona

1. **Certificado SSL/TLS**: 
   - O certificado (`certificate.crt`) e a chave privada (`private.key`) são usados para estabelecer uma conexão segura
   - O servidor usa estes arquivos para criptografar a comunicação
   - O cliente verifica a autenticidade do servidor usando o certificado

2. **Handshake TLS**:
   - Cliente e servidor negociam parâmetros de segurança
   - Verificam certificados
   - Estabelecem uma chave de sessão

3. **Comunicação Segura**:
   - Todos os dados são criptografados
   - Proteção contra interceptação
   - Garantia de integridade dos dados

## Segurança

- Utiliza TLS 1.2
- Certificados X.509
- Criptografia RSA 4096 bits
- Handshake seguro
- Proteção contra ataques Man-in-the-Middle 