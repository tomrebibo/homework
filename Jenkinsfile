pipeline {
    agent {
        docker { image 'python:3.9' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
                sh 'cp ./Dockerfile ./Dockerfile'
                sh 'cp ./app.py ./app.py'
                sh 'sleep 20'

            }
        }
    }
}
