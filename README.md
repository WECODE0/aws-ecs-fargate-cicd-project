# AWS ECS Fargate CI/CD Project

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
