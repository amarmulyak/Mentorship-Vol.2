pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
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