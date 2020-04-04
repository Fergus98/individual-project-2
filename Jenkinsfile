pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
		sh """
                     ssh -i ~/id_rsa fergus@51.140.240.158 <<EOF
                    cd individual-project-2
                    docker-compose up -d
                    """
            }
        }
    }
}
