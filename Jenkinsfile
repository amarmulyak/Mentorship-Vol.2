pipeline {
    agent any

    parameters {
        string(name: 'ENV_URL', defaultValue: '',
               description: 'URL to run the https://the-internet.herokuapp.com')
    }

    stages {
        stage('Setting Environment') {
            steps {
                echo "Setting virtualenv..."
                sh 'virtualenv .venv --python=python3.8'
                sh 'source .venv/bin/activate'

                script {
                    echo "Configuring cfg.yaml: setting base_url to ${data.base_url} "

                    def filename = 'cfg/cfg.yaml'
                    def data = readYaml file: filename

                    // Change something in the file
                    data.base_url = "${params.ENV_URL}"

                    // sh "rm $filename"
                    writeYaml file: filename, overwrite: true, data: data
                }
            }
        }
        stage('Installing requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Running Tests') {
            steps {
                sh 'pytest tests/the_internet/test_add_remove_elements.py::test_add_element'
            }
        }
    }
}