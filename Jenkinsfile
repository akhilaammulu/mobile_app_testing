pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
    }

    stages {
        stage('Set up virtual environment') {
            steps {
                script {
                    // Create virtual environment
                    sh 'python -m venv $VIRTUAL_ENV'
                    sh '$VIRTUAL_ENV/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run API Tests') {
            steps {
                script {
                    // Run API test script
                    sh '$VIRTUAL_ENV/bin/python test_api.py'
                }
            }
        }

        stage('Run Appium Tests') {
            steps {
                script {
                    // Run Appium test script
                    sh '$VIRTUAL_ENV/bin/python test_appium.py'
                }
            }
        }

        stage('Generate Test Report') {
            steps {
                script {
                    // Run pytest and generate Allure reports
                    sh '$VIRTUAL_ENV/bin/pytest --alluredir=allure-results'
                    sh 'allure serve allure-results'
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean workspace after test run
        }
    }
}
