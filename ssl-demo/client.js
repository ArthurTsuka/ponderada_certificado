const https = require('https');
const fs = require('fs');

// Configuração para aceitar certificados autoassinados (apenas para desenvolvimento)
process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 0;

// Função para fazer requisição GET
function makeGetRequest() {
    console.log('\n--- Testing HTTPS GET Request ---');
    
    const options = {
        hostname: 'localhost',
        port: 8443,
        path: '/',
        method: 'GET',
        // Para certificados autoassinados, podemos usar:
        rejectUnauthorized: false, // APENAS para desenvolvimento!
        // ca: fs.readFileSync('certificate.crt'), // Alternativa: especificar o certificado
    };

    const req = https.request(options, (res) => {
        console.log('Status Code:', res.statusCode);
        console.log('Headers:', res.headers);
        
        let data = '';
        res.on('data', (chunk) => {
            data += chunk;
        });
        
        res.on('end', () => {
            console.log('Response Body:', data);
        });
    });

    req.on('error', (e) => {
        console.error('Request error:', e.message);
    });

    req.end();
}

// Função para fazer requisição POST
function makePostRequest() {
    console.log('\n--- Testing HTTPS POST Request ---');
    
    const postData = JSON.stringify({
        msg: 'Secret data that should be protected!'
    });
    
    const options = {
        hostname: 'localhost',
        port: 8443,
        path: '/api/data',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(postData)
        },
        rejectUnauthorized: false, // APENAS para desenvolvimento!
    };

    const req = https.request(options, (res) => {
        console.log('Status Code:', res.statusCode);
        
        let data = '';
        res.on('data', (chunk) => {
            data += chunk;
        });
        
        res.on('end', () => {
            console.log('Response Body:', data);
        });
    });

    req.on('error', (e) => {
        console.error('Request error:', e.message);
    });

    req.write(postData);
    req.end();
}

// Executar os testes
console.log('Starting HTTPS Client Tests...');
console.log('Make sure the server is running on https://localhost:8443');

setTimeout(() => {
    makeGetRequest();
    setTimeout(() => {
        makePostRequest();
    }, 1000);
}, 500); 