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
        
        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f $(docker ps -aq --filter name=flask-hello-world) || true
                    docker run -d --name flask-hello-world -p 80:5000 flask-hello-world
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}