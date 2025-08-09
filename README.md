# Flask SaaS App Kubernetes Deployment

This repository contains a simple Flask application and the necessary Kubernetes manifests to deploy it on a DigitalOcean Kubernetes cluster.

## Prerequisites

- Docker installed locally
- DigitalOcean account and Container Registry
- `doctl` CLI configured and authenticated
- Access to a DigitalOcean Kubernetes cluster
- `kubectl` CLI configured for your cluster

## Steps to Deploy

### 1. Build and Push Docker Image

Build the Docker image and push it to your DigitalOcean Container Registry:

**PowerShell:**
```powershell
docker build -t flask-saas-app .
docker tag flask-saas-app:latest registry.digitalocean.com/<your-registry-name>/flask-saas-app:latest
docker push registry.digitalocean.com/<your-registry-name>/flask-saas-app:latest
```

**Bash:**
```bash
docker build -t flask-saas-app .
docker tag flask-saas-app:latest registry.digitalocean.com/<your-registry-name>/flask-saas-app:latest
docker push registry.digitalocean.com/<your-registry-name>/flask-saas-app:latest
```

Replace `<your-registry-name>` with your actual registry name.

---

### 2. Configure kubectl for Your Cluster

Download and set your kubeconfig for the target cluster:

**PowerShell:**
```powershell
doctl kubernetes cluster kubeconfig save <your-cluster-name>
```

**Bash:**
```bash
doctl kubernetes cluster kubeconfig save <your-cluster-name>
```

---

### 3. Deploy to Kubernetes

Apply the deployment and service manifests:

**PowerShell:**
```powershell
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

**Bash:**
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

---

### 4. Verify Deployment

Check that your pods and service are running:

**PowerShell:**
```powershell
kubectl get deployments
kubectl get pods
kubectl get service flask-saas-app-service
```

**Bash:**
```bash
kubectl get deployments
kubectl get pods
kubectl get service flask-saas-app-service
```

---

### 5. Access the Application

Once the service is provisioned, retrieve the external IP or DNS name:

**PowerShell:**
```powershell
kubectl get service flask-saas-app-service
```

**Bash:**
```bash
kubectl get service flask-saas-app-service
```

Access your Flask app via `http://<EXTERNAL-IP>` or the provided DNS name.

---

## File Structure

```
DODemo/
├── app.py
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
```

---

## Notes

- The deployment is set to 3 replicas for high availability.
- The service uses a LoadBalancer to expose the app externally on port 80, forwarding to port 8080 in the container.
- The deployment is configured for autoscaling, so the number of replicas may increase or decrease based on resource usage and cluster configuration.
- Make sure your image is updated in the registry before deploying