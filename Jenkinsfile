pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python env') {
            steps {
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Migrate') {
            steps {
                sh '''
                ./venv/bin/python manage.py migrate --verbosity 2
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                ./venv/bin/python manage.py test
                '''
            }
        }

    }

    post {
        success {
            echo 'Build SUCCESS ✅'
        }
        failure {
            echo 'Build FAILED ❌'
        }
    }
}