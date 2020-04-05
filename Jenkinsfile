pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
		sh """
	            ssh -o "StrictHostKeyChecking=no" fergus@51.104.226.110  << EOF
                    
                    cd individual-project-2
                    docker-compose up -d
                    """
            }
        }
    }
}
