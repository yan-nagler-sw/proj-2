pipeline {
    agent any
    stages {
        stage('cfg') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/yan-nagler-sw/proj-2.git'
            }
        }
        stage('pull-code') {
            steps {
                echo 'Pulling the code...'

                dir('~/Desktop/dev-ops-course/proj/proj-2') {
                    sh 'rm -rf run'
                    sh 'mkdir -p run'
                    sh 'cd run'
                }

// test
//                sh 'git init'
//                sh 'git remote add origin https://github.com/yan-nagler-sw/proj-2.git'
//                sh 'git pull origin master'
            }
        }
        stage('run-py-rest-app') {
            steps {
                echo 'Running Python script: rest_app.py...'
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
