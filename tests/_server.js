// Tests that reload the page serve it over http: Chromium sometimes drops localStorage on reload for file:// pages.
module.exports.serve = () => new Promise(resolve => {
  const http = require('http'), fs = require('fs'), path = require('path');
  const root = path.resolve(__dirname, '..');
  const srv = http.createServer((req, res) => {
    const f = path.join(root, decodeURIComponent(req.url.split('?')[0]).replace(/^\/+/, '') || 'index.html');
    if (!f.startsWith(root) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': f.endsWith('.html') ? 'text/html; charset=utf-8' : 'application/octet-stream' }); fs.createReadStream(f).pipe(res);
  }).listen(0, '127.0.0.1', () => { srv.unref(); resolve(`http://127.0.0.1:${srv.address().port}/index.html`); });
});

