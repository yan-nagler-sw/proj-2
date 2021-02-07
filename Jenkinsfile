pipeline {
    agent any
    stages {
        stage('pull-code') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/yan-nagler-sw/proj-2.git'
            }
        }
        stage('run-py-rest-app') {
            steps {
                echo 'Running Python script: rest_app.py...'

                sh 'PYTHONPATH=""; export PYTHONPATH="/Users/yannagler/Desktop/dev-ops-course/py/venv/lib/python3.9/site-packages/:$PYTHONPATH"; python3.9 backend_testing_db.py'
            }
        }
        stage('run-py-web-app') {
            steps {
                echo 'Running Python script: web_app.py...'
            }
        }
        stage('run-py-be-test') {
            steps {
                echo 'Running Python script: backend_testing.py...'
            }
        }
        stage('run-py-fe-test') {
            steps {
                echo 'Running Python script: frontend_testing.py...'
            }
        }
        stage('run-py-comb-test') {
            steps {
                echo 'Running Python script: combined_testing.py...'
            }
        }
        stage('run-py-clean-env') {
            steps {
                echo 'Running Python script: clean_environment.py...'
            }
        }
    }
}
