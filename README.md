# AWS ECS Fargate CI/CD Project

## Architecture diagram
  <img width="1408" height="768" alt="Architecture diagram" src="https://github.com/user-attachments/assets/c095f567-ce62-4d66-bd01-397064941cdb" />

## Overview
Built and deployed a production-style containerized application on AWS using ECS Fargate with a secure GitHub Actions CI/CD pipeline.

## Tech Stack
- AWS ECS
- AWS Fargate
- Amazon ECR
- Application Load Balancer
- ACM SSL
- GitHub Actions
- Docker
- Flask
- GoDaddy DNS
- IAM OIDC Authentication

## Features
- Dockerized Flask application
- Automated CI/CD pipeline
- HTTPS custom domain
- Load balancer routing
- Health checks
- Multi-service architecture
- Host-based routing using subdomains
- Secure OIDC authentication

## Architecture
GitHub → GitHub Actions → ECR → ECS Fargate → ALB → HTTPS Domain

## Live URLs
- https://www.rehmanilyas.site
- https://app.rehmanilyas.site

## CI/CD Workflow
1. Push code to GitHub
2. GitHub Actions builds Docker image
3. Pushes image to Amazon ECR
4. ECS service automatically updates
5. Application deployed through Fargate

## Security
- IAM roles
- OIDC authentication
- HTTPS SSL certificates
- Private container registry


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
