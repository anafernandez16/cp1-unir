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
        
        stage('Tests') {
            parallel {
                stage('Unit') {
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult:'FAILURE') {
                        sh '''
                        export PYTHONPATH=$WORKSPACE
                        chmod -R 777 $WORKSPACE
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
                                    flask run &
                                    java -jar /home/afdza/unir-devops/descargas/wiremock-standalone-3.3.1.jar --port 9090 --root-dir ./test/wiremock &
                                ''' 
                                script {
                                    def response = httpRequest(url: 'http://localhost:9090/__admin', validResponseCodes: '100:599')
                                    while (response.status != 200) {
                                        echo "${response.content}"
                                        echo 'Esperando a que WireMock se levante...'
                                        sleep 10
                                        response = httpRequest(url: 'http://localhost:9090/__admin', validResponseCodes: '100:599')

                                    }
                                }
                                  sh 'python3 -m pytest --junitxml=result-rest.xml ./test/rest'
                                
                            }    
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