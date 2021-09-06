pipeline {
    agent any

    parameters {
        string(name: 'ENV_URL', defaultValue: '',
               description: 'URL to run the https://the-internet.herokuapp.com')
    }

    stages {
        stage('Setting URL') {
            steps {
                // No need to set up venv as Jenkins is already running under venv
                sh 'virtualenv venv --python=python3.8'
                sh 'source venv/bin/activate'

                script {
                    def filename = 'cfg/cfg.yaml'
                    def data = readYaml file: filename

                    // Change something in the file
                    data.base_url = "${params.ENV_URL}"

                    // sh "rm $filename"
                    writeYaml file: filename, overwrite: true, data: data

                    echo "URL is ${data.base_url} "
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