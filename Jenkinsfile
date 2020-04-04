pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
		sh """
	            vmuser='fergus@52.151.118.99'
                    vmpass='Password1...'
                    sshpass -p ${vmpass} ssh -o StrictHostKeyChecking=no ${vmuser}<<eof
                    
                    cd individual-project-2
                    docker-compose up -d
                    """
            }
        }
    }
}
