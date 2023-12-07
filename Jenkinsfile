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
    
        stage('Result') {
            steps {
                junit 'result*.xml'
            }
        }
    }
}