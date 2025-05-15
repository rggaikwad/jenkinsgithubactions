# Flask Hello World Application

A simple Flask application with CI/CD pipeline integration using GitHub Actions and Jenkins.

## Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Docker

Build and run using Docker:
```bash
docker build -t flask-hello-world .
docker run -p 5000:5000 flask-hello-world
```

## CI/CD Pipeline

This project includes:
- GitHub Actions workflow for automated testing and building
- Jenkins pipeline for deployment
- Docker containerization

### GitHub Actions
The workflow automatically runs on push to main branch and pull requests, performing:
- Python dependency installation
- Running tests
- Building Docker image
- Triggering Jenkins build

### Jenkins
The Jenkins pipeline includes stages for:
- Code checkout
- Building Docker image
- Running tests
- Deployment

## Testing

Run tests using pytest:
```bash
pytest
``` 