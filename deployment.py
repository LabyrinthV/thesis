import subprocess

# Set variables
resource_group_name = 'your_resource_group_name'
aks_cluster_name = 'your_aks_cluster_name'
deployment_yaml = '''
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app-container
        image: myregistry.azurecr.io/my-app:latest
        ports:
        - containerPort: 80
'''

service_yaml = '''
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
'''

# Get AKS credentials
subprocess.run(['az', 'aks', 'get-credentials', '--resource-group', resource_group_name, '--name', aks_cluster_name])

# Write deployment YAML to file
with open('deployment.yaml', 'w') as f:
    f.write(deployment_yaml)

# Apply deployment
subprocess.run(['kubectl', 'apply', '-f', 'deployment.yaml'])

# Write service YAML to file
with open('service.yaml', 'w') as f:
    f.write(service_yaml)

# Apply service
subprocess.run(['kubectl', 'apply', '-f', 'service.yaml'])