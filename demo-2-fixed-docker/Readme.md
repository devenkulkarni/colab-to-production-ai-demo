## Demo 2 - Fixed (Docker)

Run:
docker build -t ai-app .
docker run -p 8000:8000 ai-app

Test:
http://localhost:8000/chat?prompt=Hello

Fix:
Use host.docker.internal

Result:
✅ Works locally

Limitation:
❌ Will NOT work in Kubernetes
