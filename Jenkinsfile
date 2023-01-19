pipeline {
    agent {
        docker { image 'docker:latest' }
    }
    stages {
        stage('Test1') {
            steps {
                sh 'docker version'
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
