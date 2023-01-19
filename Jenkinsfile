pipeline {
    agent {
        docker { image 'docker:latest' }
    }
    environment {
     dockerhub=credentials('DOCKERHUB')
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
                sh 'echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin'
                sh 'docker push tomrebibo/app:4 '

            }



        }

        stage('cleanup'){
            steps{
                sh 'docker system prune -af'
            }
            
        }
    }
}
