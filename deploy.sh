#!/bin/bash

# Exit on error
set -e

# Create Kind cluster
sudo kind create cluster --name tiredful || { echo "Kind cluster already exists."; }

# Load Docker image into Kind
sudo docker pull natalieaoya/tiredful:latest
sudo kind load docker-image natalieaoya/tiredful:latest --name tiredful

# Apply Kubernetes manifest
mkdir ~/.kube || { echo "Directory already exists."; }
sudo kind get kubeconfig --name tiredful > ~/.kube/config
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Wait a few seconds for service to start
sleep 30
