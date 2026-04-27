## Demo 1 - Broken

Run:
`docker build -t ai-app .`

`docker run -p 8000:8000 demo1-aiapp`

Test:
http://localhost:8000/chat?prompt=Hello

Expected:
❌ Connection refused
