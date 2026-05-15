# AWS ECS Fargate CI/CD Project

## Architecture diagram
  <img width="1408" height="768" alt="Architecture diagram" src="https://github.com/user-attachments/assets/c095f567-ce62-4d66-bd01-397064941cdb" />

## Project Overview

This project demonstrates a production-style full stack cloud architecture deployed on AWS using modern DevOps practices.

The architecture includes:

* React frontend hosted on Amazon S3
* CloudFront CDN integration
* Cloudflare DNS management
* Flask backend API deployed on Amazon ECS Fargate
* Docker containerization
* GitHub Actions CI/CD pipeline
* Amazon ECR image registry
* Application Load Balancer with HTTPS
* ACM SSL certificate integration
* Amazon RDS MySQL database
* Secure VPC networking and security groups

---

## Architecture

```text
Frontend (React + S3 + CloudFront)
        ↓
Cloudflare DNS
        ↓
Application Load Balancer (HTTPS)
        ↓
Amazon ECS Fargate Backend
        ↓
Amazon RDS MySQL
```

---

## Tech Stack

* AWS ECS Fargate
* AWS ECR
* AWS RDS MySQL
* AWS S3
* AWS CloudFront
* Application Load Balancer
* AWS ACM
* Docker
* GitHub Actions
* Flask
* React
* Cloudflare
* Python
* PyMySQL

---

## Features

* End-to-end CI/CD pipeline
* Dockerized backend deployment
* Secure HTTPS configuration
* Host-based routing
* REST API integration
* React frontend integration
* Form submission and database persistence
* Cloud-native infrastructure
* Health checks and load balancing
* Production-style deployment architecture

---

## API Endpoints

### Health Check

```bash
GET /health
```

### Get Leads

```bash
GET /api/leads
```

### Create Lead

```bash
POST /api/leads
```

---

## Frontend

Frontend application is deployed using:

* Amazon S3 Static Hosting
* Amazon CloudFront
* Cloudflare DNS

Frontend URL:

```text
https://frontend.rehmanilyas.site
```

---

## Backend

Backend API is deployed on:

* Amazon ECS Fargate
* Application Load Balancer
* Docker containers

Backend URL:

```text
https://www.rehmanilyas.site
```

---

## Database

Amazon RDS MySQL is used for persistent data storage.

Security configuration:

* Private database access
* Security group restricted to ECS tasks only
* No public database exposure

---

## CI/CD Pipeline

```text
GitHub Actions
    ↓
Docker Build
    ↓
Amazon ECR
    ↓
Amazon ECS Fargate Deployment
```

---

## Deployment Highlights

* Secure SSL integration using AWS ACM
* Custom domain configuration
* Cloud-native scalable architecture
* Automated deployments through GitHub Actions
* Frontend and backend separation
* Production-style infrastructure design

---

## Author

Rehman Ilyas


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
