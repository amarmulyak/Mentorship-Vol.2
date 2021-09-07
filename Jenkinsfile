pipeline {
    agent any

    parameters {
        string(name: 'ENV_URL', defaultValue: '',
               description: 'URL to run the https://the-internet.herokuapp.com')
    }

    stages {
        stage('Setting URL') {
            steps {
                // Create and activate virtualenv
                // sh '. activate_venv.sh'

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
        stage('Installing requirements / Running Tests') {
            steps {
                sh """
                virtualenv venv --python=python3.8
                . venv/bin/activate
                python --version
                pip install -r requirements.txt
                pytest tests/the_internet/test_add_remove_elements.py::test_add_element
                """
            }
        }
    }
}