pipeline {
    agent any

    stages {
        stage('Test Run') {
            steps {
                /* `make check` returns non-zero on test failures,
                * using `true` to allow the Pipeline to continue nonetheless
                */
                sh 'pytest tests/'
            }
        }
    }
}