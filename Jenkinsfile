pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t flask-hello-world .'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python -m pytest'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-hello-world'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
} 