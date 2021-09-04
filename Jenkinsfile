pipeline {
    agent any

    parameters {
        string(name: 'ENV_URL', defaultValue: 'https://the-internet.herokuapp.com', description: 'URL to run the')
    }

    stages {
        stage('Setting URL') {
            steps {
                echo "Reading yaml ..."
                def datas = readYaml file: 'cfg/cfg.yml'
                echo "URL is ${datas.base_url} "
            }
        }
        stage('Installing requirements') {
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