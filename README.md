# 🌐 Production-Ready Containerized REST API on AWS ECS Fargate

**Terraform • FastAPI • Docker • PostgreSQL • Cloud Architecture**

---

# 📌 Project Summary

This project demonstrates the design and deployment of a **highly available, cloud-native backend API** running on **AWS ECS Fargate**, with infrastructure fully provisioned using **Terraform (Infrastructure as Code)**.

The system follows modern DevOps and cloud architecture principles:

* Infrastructure defined entirely as code
* Containerized microservice deployment
* Secure VPC networking
* Automated scaling
* Observability through CloudWatch
* Reproducible local development using Docker Compose

The objective of this project is to simulate a **real-world production architecture** aligned with responsibilities expected from a Cloud Architect / DevOps Engineer.

---

# 🧠 Architecture Overview

## 🔷 High-Level Design

This solution deploys a scalable API backend behind an Application Load Balancer, with compute and database layers isolated inside private subnets.

### Architecture Flow

```
Client Request
     ↓
Application Load Balancer (Public Subnets)
     ↓
ECS Fargate Tasks (Private Subnets)
     ↓
Amazon RDS PostgreSQL (Private Subnets)
```

---

## 🏗 AWS Components

| Component           | Purpose                                   |
| ------------------- | ----------------------------------------- |
| VPC                 | Isolated network for all services         |
| Public Subnets      | Hosts Application Load Balancer           |
| Private Subnets     | Hosts ECS tasks and RDS database          |
| Internet Gateway    | Enables external traffic to ALB           |
| Security Groups     | Controls service-to-service communication |
| ECS Cluster         | Container orchestration                   |
| ECS Fargate Service | Serverless container execution            |
| Amazon ECR          | Docker image registry                     |
| RDS PostgreSQL      | Managed relational database               |
| CloudWatch Logs     | Application observability                 |
| Auto Scaling        | Dynamic scaling based on CPU usage        |

---

# 📁 Repository Structure

```
.
├── api/
│   ├── src/
│   │   ├── main.py
│   │   ├── config.py
│   │   └── models.py
│   ├── tests/
│   │   └── test_api.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── versions.tf
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# ⚙️ Local Development Setup

## 1️⃣ Start Local Environment

```
docker-compose up --build
```

This launches:

* FastAPI service
* PostgreSQL database container

API will be available at:

```
http://localhost:8000
```

---

## 2️⃣ Test Local API

### Health Check

```
curl http://localhost:8000/health
```

Expected:

```
{"status":"healthy"}
```

---

### Create Item

```
curl -X POST http://localhost:8000/items \
-H "Content-Type: application/json" \
-d '{"name":"local-test","description":"docker compose"}'
```

---

### Get Items

```
curl http://localhost:8000/items
```

---

# 🐳 Containerization Strategy

The API is built using a **multi-stage Dockerfile**:

## Builder Stage

* Installs Python dependencies
* Keeps image lightweight

## Runtime Stage

* Copies only required runtime files
* Minimizes attack surface
* Optimized for ECS Fargate deployment

Benefits:

* Smaller image size
* Faster deployment
* Improved security posture

---

# ☁️ Infrastructure Deployment (Terraform)

## 1️⃣ Initialize Terraform

```
cd terraform
terraform init
```

---

## 2️⃣ Deploy AWS Infrastructure

```
terraform apply
```

Provisioned resources include:

* VPC with public/private subnet design
* Internet Gateway and Route Tables
* Security Groups
* Amazon ECR Repository
* ECS Cluster + Fargate Service
* Application Load Balancer
* Target Group and Listener
* RDS PostgreSQL Instance
* CloudWatch Log Group
* Auto Scaling Policy

---

## 3️⃣ Retrieve ALB Endpoint

```
terraform output alb_dns
```

Example:

```
task12-alb-xxxx.us-east-1.elb.amazonaws.com
```

---

# 🌍 Testing the Live Deployment

### Health Endpoint

```
curl http://<alb_dns>/health
```

---

### Create Item

```
curl -X POST http://<alb_dns>/items \
-H "Content-Type: application/json" \
-d '{"name":"aws-live","description":"fargate success"}'
```

---

### Fetch Items

```
curl http://<alb_dns>/items
```

---

# 🔐 Environment Configuration

Example `.env.example`:

```
DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase
```

Sensitive values are injected via environment variables inside ECS Task Definition.

---

# 🧪 Unit Testing

Run tests locally:

```
cd api
pytest
```

Example output:

```
3 passed
```

Tests validate:

* Health endpoint
* Item creation
* Item retrieval

---

# 📚 API Reference

## GET /health

Checks service availability.

Response:

```
200 OK
{"status":"healthy"}
```

---

## POST /items

Creates a new database record.

Request Body:

```
{
  "name": "string",
  "description": "string"
}
```

Response:

```
201 Created
{
  "id": "uuid",
  "name": "...",
  "description": "...",
  "created_at": "timestamp"
}
```

---

## GET /items

Returns all items stored in PostgreSQL.

Response:

```
200 OK
[
  {...}
]
```

---

# 📊 Observability

Logging is integrated with AWS CloudWatch:

* Container logs streamed automatically
* Health checks monitored via ALB
* ECS task lifecycle events available

---

# 📈 Auto Scaling Configuration

ECS Service uses Target Tracking Scaling:

* Metric: ECSServiceAverageCPUUtilization
* Target CPU Usage: **70%**
* Minimum Tasks: 1
* Maximum Tasks: 3

This enables automatic scaling under load.

---

# 🔒 Security Architecture

Security Groups enforce least-privilege communication:

* ALB → accepts public HTTP traffic
* ECS Tasks → accept traffic only from ALB SG
* RDS Database → accepts traffic only from ECS SG
* Database is NOT publicly accessible

---

# 🧹 Infrastructure Cleanup

To avoid AWS charges:

```
terraform destroy
```

---

# 🛠 Technology Stack

* FastAPI
* SQLAlchemy
* PostgreSQL
* Docker
* Terraform
* AWS ECS Fargate
* Amazon RDS
* Amazon ECR
* Application Load Balancer
* AWS CloudWatch

---

# 🎯 Skills Demonstrated

* Infrastructure as Code (Terraform)
* Serverless Container Deployment
* Secure VPC Networking Design
* Auto-Scaling Strategy
* Production Logging & Monitoring
* Container Optimization
* API Development & Testing

---

# 📸 Suggested Screenshots for Submission

Include:

* ALB `/health` response
* POST `/items` request output
* GET `/items` response
* ECS Service running tasks
* CloudWatch Logs stream

---

# 👨‍💻 Author

**Bharghav Sai Marla**
Cloud Architecture & DevOps Engineering Project

---
