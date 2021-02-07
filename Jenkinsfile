pipeline {
    agent any
        environment {
            usr = 'yannagler'
            py_dir = "/Users/${usr}/Desktop/dev-ops-course/py"
        }
    stages {
        stage('handle-git') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/yan-nagler-sw/proj-2.git'
            }
        }
        stage('handle-prereq') {
            steps {
                echo 'Running Python script: backend_testing_db.py...'
                echo "py_dir: ${py_dir}""
                sh '''
                    export PYTHONPATH="/Users/yannagler/Desktop/dev-ops-course/py/venv/lib/python3.9/site-packages/:$PYTHONPATH"
                    python3.9 backend_testing_db.py
                '''

                echo 'Copying Selenium WebDriver - Chrome...'
                sh '''
                    cp /Users/yannagler/Desktop/dev-ops-course/env/chromedriver .
                '''
            }
        }
/*
        stage('run-py-rest-app') {
            steps {
                echo 'Running Python script: rest_app.py...'
                sh '''
                    export PYTHONPATH="/Users/yannagler/Desktop/dev-ops-course/py/venv/lib/python3.9/site-packages/:$PYTHONPATH"
                    nohup python3.9 rest_app.py &
                    python3.9 backend_testing_rest.py
                '''
            }
        }
        stage('run-py-web-app') {
            steps {
                echo 'Running Python script: web_app.py...'
                sh '''
                    export PYTHONPATH="/Users/yannagler/Desktop/dev-ops-course/py/venv/lib/python3.9/site-packages/:$PYTHONPATH"
                    nohup python3.9 web_app.py &
                '''
            }
        }
        stage('run-py-be-test') {
            steps {
                echo 'Running Python script: backend_testing.py...'
                sh '''
                    export PYTHONPATH="/Users/yannagler/Desktop/dev-ops-course/py/venv/lib/python3.9/site-packages/:$PYTHONPATH"
                    python3.9 backend_testing.py
                '''
            }
        }
        stage('run-py-fe-test') {
            steps {
                echo 'Running Python script: frontend_testing.py...'
                sh '''
                    export PYTHONPATH="/Users/yannagler/Desktop/dev-ops-course/py/venv/lib/python3.9/site-packages/:$PYTHONPATH"
                    python3.9 frontend_testing.py
                '''
            }
        }
        stage('run-py-comb-test') {
            steps {
                echo 'Running Python script: combined_testing.py...'
                sh '''
                    export PYTHONPATH="/Users/yannagler/Desktop/dev-ops-course/py/venv/lib/python3.9/site-packages/:$PYTHONPATH"
                    python3.9 combined_testing.py
                '''
            }
        }
        stage('run-py-clean-env') {
            steps {
                echo 'Running Python script: clean_environment.py...'
                sh '''
                    export PYTHONPATH="/Users/yannagler/Desktop/dev-ops-course/py/venv/lib/python3.9/site-packages/:$PYTHONPATH"
                    python3.9 clean_environment.py
                '''
            }
        }
*/
    }
}
