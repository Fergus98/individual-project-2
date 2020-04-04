pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
		sh """
                     ssh fergus@51.140.240.158 <<EOF
                    cd individual-project-2
                    docker-compose up -d
                    """
            }
        }
    }
}
