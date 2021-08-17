pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'sudo apt-get install python3-tk python3-dev'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Running Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}