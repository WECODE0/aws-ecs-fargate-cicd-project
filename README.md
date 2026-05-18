# AWS ECS Fargate CI/CD Project

A production-style AWS DevOps project demonstrating containerized application deployment, CI/CD automation, HTTPS custom domain integration, and event-driven ECS auto-start/auto-stop infrastructure optimization.

## Architecture diagram
  <img width="1408" height="768" alt="Architecture diagram" src="https://github.com/user-attachments/assets/c095f567-ce62-4d66-bd01-397064941cdb" />

---

# Project Architecture

```text
Frontend (S3 Static Hosting)
        ↓
API Gateway Wakeup Endpoint
        ↓
AWS Lambda
        ↓
Amazon ECS Fargate Backend
        ↓
Application Load Balancer
        ↓
RDS MySQL Database
```

## Auto Stop Workflow

```text
No Traffic on ALB
        ↓
CloudWatch Alarm
        ↓
EventBridge Rule
        ↓
AWS Step Functions
        ↓
Lambda Function
        ↓
ECS Desired Count = 0
```

## Auto Start Workflow

```text
Frontend Page Load
        ↓
React useEffect Trigger
        ↓
API Gateway /wakeup
        ↓
Lambda Function
        ↓
ECS Desired Count = 1
```

---

# Features

* Dockerized Flask backend
* React + Vite frontend
* AWS ECS Fargate deployment
* Amazon ECR image management
* GitHub Actions CI/CD pipeline
* HTTPS custom domain with ACM SSL
* Application Load Balancer integration
* AWS Lambda-based ECS scaling
* CloudWatch traffic monitoring
* EventBridge automation
* AWS Step Functions orchestration
* ECS automatic stop on idle traffic
* ECS automatic wake-up on frontend access
* CORS handling between frontend and backend
* Production-style serverless-inspired architecture
* Cost optimization using scale-to-zero strategy

---

# AWS Services Used

* Amazon ECS Fargate
* Amazon ECR
* AWS Lambda
* Amazon API Gateway
* AWS Step Functions
* Amazon EventBridge
* Amazon CloudWatch
* Application Load Balancer
* AWS Certificate Manager (ACM)
* Amazon Route 53 / GoDaddy DNS
* Amazon S3 Static Hosting
* Amazon RDS MySQL
* GitHub Actions

---

# CI/CD Workflow

```text
GitHub Push
    ↓
GitHub Actions
    ↓
Docker Image Build
    ↓
Push Image to Amazon ECR
    ↓
Update ECS Service
    ↓
Automatic Deployment
```

---

# Tech Stack

* Python Flask
* React
* Vite
* Docker
* AWS ECS
* AWS Fargate
* GitHub Actions
* MySQL
* Nginx
* AWS Lambda

---

# Key Learning Outcomes

* Implemented production-grade container deployment on AWS
* Built automated CI/CD pipelines using GitHub Actions
* Configured HTTPS custom domains with SSL certificates
* Implemented event-driven infrastructure automation
* Designed ECS scale-to-zero architecture for cost optimization
* Integrated CloudWatch, EventBridge, Step Functions, and Lambda
* Handled frontend/backend CORS communication securely

---

# Future Improvements

* Add authentication and authorization
* Implement Terraform infrastructure as code
* Add monitoring dashboards with CloudWatch
* Add autoscaling based on CPU and memory utilization
* Implement blue/green deployments

---

# Author

Rehman Ilyas

LinkedIn:
https://www.linkedin.com/in/rehman-ilyas


## ECP Repo
<img width="740" height="341" alt="ECR_repo" src="https://github.com/user-attachments/assets/fad3407e-698d-42cc-a5bc-39b0e741726e" />

## ECS SERVICES 
<img width="738" height="380" alt="ECS_Services" src="https://github.com/user-attachments/assets/0a60217f-f449-4eeb-b8ec-0da0ebf3aeba" />

## Github Action 
<img width="673" height="431" alt="Github_action" src="https://github.com/user-attachments/assets/b0d5ceea-dd0b-4dc3-a6e6-166fde5e104c" />

## Loadbalancer 
<img width="751" height="289" alt="Loadbalancer_Rule" src="https://github.com/user-attachments/assets/caadd925-2411-4c3e-85a9-acc088f82d57" />

## Target Group 
<img width="761" height="258" alt="Target_Group" src="https://github.com/user-attachments/assets/3e3b11ea-1958-4fd7-b648-ad8a717f044e" />
