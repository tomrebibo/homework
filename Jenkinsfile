pipeline {
    agent any
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

        stage('deploy'){
            steps{
                sshagent(['ssh-master']) {
                    sh 'ssh ec2-user@3.8.199.162 pwd '
                    }
            }
        }

        stage('cleanup'){
            steps{
                sh 'docker system prune -af'
            }
            
        }
    }
}
