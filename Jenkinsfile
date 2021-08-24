pipeline {
    agent any

    stages {
        stage('Set Up') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Running Tests') {
            steps {
                sh 'pytest tests/the_internet/test_add_remove_elements.py'
            }
        }
    }
}