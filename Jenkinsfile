pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
		sh """
	            ssh -o "StrictHostKeyChecking=no" fergus@51.104.17.65  << EOF
                    
                    cd individual-project-2
                    docker-compose up -d
                    """
            }
        }
    }
}
