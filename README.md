Disaster Decision Intelligence Platform
Python FastAPI Docker PostgreSQL AWS EC2 Machine Learning

An AI-powered cloud-based platform for disaster monitoring, data processing, and intelligent decision support using Machine Learning, FastAPI, PostgreSQL, Docker, and AWS EC2.

📌 Project Overview
The Disaster Decision Intelligence Platform is an end-to-end cloud-based system that collects earthquake and weather information, processes it through an ETL pipeline, stores it in PostgreSQL, performs machine learning-based disaster prediction, and exposes REST APIs using FastAPI.

The complete application is containerized using Docker and deployed on AWS EC2, making it easily accessible through interactive Swagger API documentation.

🚀 Features
✅ Earthquake Data Processing

✅ Weather Data Integration

✅ ETL Pipeline

✅ Machine Learning Prediction

✅ Disaster Decision Engine

✅ FastAPI REST APIs

✅ PostgreSQL Database

✅ Dockerized Deployment

✅ AWS EC2 Cloud Hosting

✅ Interactive Swagger Documentation

🏗️ System Architecture
image
docs/architecture.png
![Architecture](docs/architecture.png)
⚙️ Technology Stack
Category	Technologies
Programming Language	Python
Backend	FastAPI
Machine Learning	Scikit-learn
Database	PostgreSQL
Data Processing	Pandas, NumPy
ORM	SQLAlchemy
API Documentation	Swagger UI
Containerization	Docker, Docker Compose
Cloud Platform	AWS EC2
Version Control	Git & GitHub
📂 Project Structure
disaster-decision-intelligence-platform/

│

├── data/
│ ├── raw/
│ └── processed/
│
├── docs/
│ ├── architecture.png
│ ├── swagger_home.png
│ ├── predict_endpoint.png
│ ├── latest_earthquake.png
│ ├── docker_ps.png
│ ├── aws_ec2.png
│ └── powerbi_dashboard.png
│
├── ml/
│
├── src/
│ ├── api.py
│ ├── decision_engine.py
│ ├── predictor.py
│ ├── load.py
│ ├── load_weather.py
│ ├── weather.py
│ └── database/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
🔄 System Workflow
Earthquake Dataset
        │
        ▼
ETL Pipeline
        │
        ▼
Processed Dataset
        │
        ▼
PostgreSQL Database
        │
        ▼
Machine Learning Model
        │
        ▼
Decision Intelligence Engine
        │
        ▼
FastAPI REST API
        │
        ▼
Swagger UI
        │
        ▼
AWS EC2 Deployment
📡 REST API Endpoints
Method	Endpoint	Description
GET	/health	API Health Check
GET	/latest-earthquake	Retrieve latest earthquake information
POST	/predict	Predict disaster severity
📸 API Documentation (Swagger UI)
**image **

![Swagger UI](docs/swagger_home.png)
`
📸 Latest Earthquake Endpoint
WhatsApp Image 2026-07-17 at 4 14 00 PM
![Latest Earthquake](docs/latest_earthquake.png)
📸 Docker Containers
The application is fully containerized using Docker.

image
docker ps
![Docker Containers](docs/docker_ps.png)
📸 AWS EC2 Deployment
The platform is deployed on an Ubuntu AWS EC2 instance.

image
![AWS EC2](docs/aws_ec2.png)
📊 Power BI Dashboard
The processed disaster data can be visualized using an interactive Power BI dashboard.

image
![Power BI Dashboard](docs/powerbi_dashboard.png)
🧠 Machine Learning Pipeline
Data Collection
Data Cleaning
Feature Engineering
Model Training
Model Evaluation
Model Serialization
Prediction API Deployment
🐳 Docker Deployment
Build

docker compose build
Run

docker compose up -d
Stop

docker compose down
☁️ AWS Deployment
The application is deployed on:

AWS EC2 Ubuntu Instance
Docker
Docker Compose
PostgreSQL
FastAPI
Swagger UI
💻 Local Installation
Clone Repository

git clone https://github.com/<Akshaya27111>/disaster-decision-intelligence-platform.git
Move into Project

cd disaster-decision-intelligence-platform
Build

docker compose build
Run

docker compose up -d
🎯 Future Enhancements
HTTPS Support
CI/CD Pipeline
Cloud Monitoring
Real-time Alert Notifications
Dashboard Enhancements
