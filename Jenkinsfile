pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                sudo docker-compose up -d
            }
        }
    }
}
