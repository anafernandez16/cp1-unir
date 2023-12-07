pipeline {
    agent any

    stages {
        stage('Get Code') {
            steps {
                git 'https://github.com/anafernandez16/cp1-unir.git'
            }
        }
        
        stage('Build') {
            steps {
            echo 'Esto es python, no se compila'
            echo WORKSPACE
            sh 'ls'
            }
        }

        stage('Unit') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult:'FAILURE') {
                sh '''
                export PYTHONPATH=$WORKSPACE
                chmod -R 777 /var/lib/jenkins/workspace/CP1-A/
                python3 -m pytest --junitxml=result-unit.xml ./test/unit
            '''
                }
            }
        }

        stage('Rest') {
            steps {
                sh '''
                    export FLASK_APP=app/api.py
                    export FLASK_ENV=development
                    start flask run
                    start java -jar /home/afdza/unir-devops/descargas/wiremock-standalone-3.3.1.jar --port 9090 --root-dir ./test/wiremock
                    set PYTHONPATH=$WORKSPACE
                    chmod -R 777 /var/lib/jenkins/workspace/CP1-A/
                    python3 -m pytest --junitxml=result-rest.xml .test/rest
                '''
            }    
        }
    
        stage('Result') {
            steps {
                junit 'result*.xml'
            }
        }
    }
}