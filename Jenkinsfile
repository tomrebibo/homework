pipeline {
    agent {
        docker { image 'python:3.9' }
    }
    stages {
        stage('Test1') {
            steps {
                sh 'python --version'
            }
        }

        stage('build'){
            steps{
                sh 'docker build -t tomrebibo/app:4 .'
            }



        }

        stage('cleanup'){
            steps{
                sh 'docker system prune -a'
            }
            
        }
    }
}
