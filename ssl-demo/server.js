const https = require('https');
const fs = require('fs');

const options = {
    key: fs.readFileSync('private.key'),
    cert: fs.readFileSync('certificate.crt'),
    // ca: fs.readFileSync('ca-bundle.crt'), // Opcional, para cadeias confiáveis
};

const server = https.createServer(options, (req, res) => {
    console.log('HTTPS Server received request from:', req.connection.remoteAddress);
    console.log('Method:', req.method);
    console.log('URL:', req.url);
    
    // Handle different routes
    if (req.url === '/api/data' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });
        req.on('end', () => {
            console.log('HTTPS Server received:', JSON.parse(body));
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({
                received: JSON.parse(body),
                encrypted: true,
                timestamp: new Date().toISOString()
            }));
        });
    } else {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Secure Connection Established via HTTPS!\nTime: ' + new Date().toISOString());
    }
});

const PORT = 8443; // Usando porta 8443 ao invés de 443 para não precisar de sudo
server.listen(PORT, () => {
    console.log(`HTTPS Server running on https://localhost:${PORT}`);
    console.log('Certificate: certificate.crt');
    console.log('Private Key: private.key');
});

server.on('error', (err) => {
    console.error('Server error:', err);
}); 