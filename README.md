# Kubernetes Microservices Deployment

## Project Overview

This project demonstrates the containerization and Kubernetes deployment of a microservices-based application using Docker, Kubernetes, Minikube, Prometheus, and Grafana.

The application consists of three independent microservices:

- **Frontend Microservice** – Handles frontend service requests.
- **Backend Microservice** – Provides backend application functionality.
- **Database Microservice** – Uses SQLite for data storage and CRUD operations.

## Technologies Used

- Docker & Docker Desktop
- Kubernetes
- Minikube
- kubectl
- Python & Flask
- SQLite
- Kubernetes YAML
- Helm
- Prometheus
- Grafana
- Git & GitHub

## Project Structure

```text
kubernetes-deployment/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── database/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── k8s/
│   ├── backend-configmap.yaml
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── database-deployment.yaml
│   ├── database-pvc.yaml
│   ├── database-service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   └── ingress.yaml
│
├── .gitignore
└── README.md
```

## Docker Containerization

Each microservice has its own Dockerfile and Docker image.

Images created:

- `task2-backend:1.0`
- `task2-backend:2.0`
- `task2-frontend:1.0`
- `task2-database:3.0`

## Kubernetes Deployment

The application is deployed locally on a Minikube Kubernetes cluster.

Kubernetes resources implemented:

- Deployments for all three microservices
- ClusterIP and NodePort Services
- NGINX Ingress
- ConfigMap
- Kubernetes Secret
- Persistent Volume Claim (PVC)

## Rolling Updates and Rollbacks

Implemented and tested Kubernetes rolling updates by upgrading the backend container image.

Also performed a rollback to a previous deployment revision using Kubernetes rollout commands.

## Persistent Storage

Configured a 1Gi Persistent Volume Claim for the database microservice.

SQLite database storage is mounted at `/data`.

Verified data persistence by deleting and recreating the database pod. Previously stored user data remained available after pod recreation.

## Horizontal Pod Autoscaling

Configured Horizontal Pod Autoscaler (HPA) for the backend deployment.

- Minimum replicas: 2
- Maximum replicas: 5
- CPU utilization target: 50%

Successfully tested scaling up under load and scaling down after load removal.

## Monitoring with Prometheus and Grafana

Installed Prometheus and Grafana using Helm.

Configured Prometheus as a Grafana data source and created a Kubernetes Monitoring Dashboard with the following panels:

1. Kubernetes Pods Information
2. Prometheus Service Health Status
3. Kubernetes Pod CPU Utilization
4. Kubernetes Pod Memory Utilization

## Running the Project Locally

### Prerequisites

- Docker Desktop
- Minikube
- kubectl
- Helm

### Start Minikube

```bash
minikube start --driver=docker
```

### Deploy Kubernetes Resources

```bash
kubectl apply -f k8s/
```

### Check Deployments

```bash
kubectl get deployments
```

### Check Services

```bash
kubectl get services
```

### Check Pods

```bash
kubectl get pods
```

## Monitoring Access

Start Grafana port forwarding:

```bash
kubectl port-forward -n monitoring svc/grafana 3000:80
```

Open Grafana:

`http://localhost:3000`

## Project Status

Local Kubernetes deployment, microservices containerization, persistent storage, autoscaling, rolling updates, rollbacks, and monitoring have been implemented and tested.


## Author

Javaria Afzal

GitHub: [JavariaAfzal](https://github.com/JavariaAfzal)

Project Repository: [kubernetes-deployment](https://github.com/JavariaAfzal/kubernetes-deployment)
