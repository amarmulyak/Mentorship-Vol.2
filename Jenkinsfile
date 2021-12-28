pipeline {
    agent any

    parameters {
        string(name: 'ENV_URL', defaultValue: '',
               description: 'URL to run the https://the-internet.herokuapp.com')
    }

    stages {
        stage('Setting URL') {
            steps {
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
        stage('Setting environment') {
            steps {
                sh """
                virtualenv venv
                . venv/bin/activate
                pip install -r requirements.txt
                """
            }
        }
        stage('Running Tests') {
            steps {
                sh """
                . venv/bin/activate
                pytest tests/the_internet/test_add_remove_elements.py::test_add_element
                """
            }
        }
    }
    post {
        always  {
            script {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'tests/allure_result_folder']]
                ])
            }
        }
    }
}