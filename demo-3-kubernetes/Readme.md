## Demo 3 - Kubernetes

kubectl apply -f ollama-deployment.yaml

Test:
kubectl port-forward svc/ai-app 8000:80

http://localhost:8000/ask?prompt=Hello 

OR

kubectl run test --rm -it --image=curlimages/curl -- sh
curl http://ollama:11434/api/generate -d '{ "model": "llama3.1", "prompt": "Explain Kubernetes in one line", "stream" : false }'

Result:
✅ Works using service DNS
