### This is a good beginning, a long journey to be a little better everyday
1. Postgres
Deployment (1 replica)
PersistentVolumeClaim (for /var/lib/postgresql/data)
Service (ClusterIP for internal API access)

2. FastAPI backend
Deployment (replicas = 2+ for scaling)
Service (ClusterIP for Nginx to talk to fastapi-svc:8000)
Environment variables via ConfigMap and Secret

3. Frontend (nginx + static HTML)
Deployment
Service (ClusterIP inside, or LoadBalancer/NodePort for browser access)
Nginx config via ConfigMap