pipeline {
    agent {
        docker { image 'docker:latest' }
    }
    environment {
     dockerhub=credentials('DOCKERHUB')
    }
    stages {
        stage('build'){
            steps{
                sh 'docker build -t tomrebibo/app:${BUILD_NUMBER} .'
                sh 'echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin'
                sh 'docker push tomrebibo/app:${BUILD_NUMBER} '

            }

        }

        stage('deploy'){
            steps{
                sshagent(['ssh-master']) {
                    sh 'scp -r -o StrictHostKeyChecking=no ./app-chart/ ec2-user@3.8.199.162:/home/ec2-user/'
                    script{
                        sh "ssh ec2-user@3.8.199.162 helm upgrade --set-string container.tag=${BUILD_NUMBER} --install my-app /home/ec2-user/app-chart"
                    }
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
