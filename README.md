# postBasedXSS
Demo of some ways to practically exploit post based reflected XSS



Requirements:
flask


Install requirements with:
pip install -r requirements.txt

Run the server with:
python postXssServer.py


In your browser (preferably configured to proxy through Burp) navigate to:
http://localhost:80



Demos ways to exploit POST based reflected XSS
* Method Tampering
* CSRF
* Spoofed JSON CSRF Attack



@hoodoer
Drew.Kirkpatrick@TrustedSec.com