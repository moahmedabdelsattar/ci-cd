pipeline{
    agent any 
    environment{
            IMAGE= "dev-app"
    }
    
    }
    stages{
        stage('check'){
            steps{
                sh '''
                ls
                test -f Dockerfile
                test -f requirements.txt
                '''
            }
        }
        stage('build image'){
            steps{
                sh '''
                docker build -t dev-app .
                ... 
            }
        }
                                 
        stage('check image'){
            steps{
                sh '''
                docker image ls ${IMAGE}
                '''
            }
        }
        stage('Docker Login') {
    steps {
        withCredentials([
            usernamePassword(
                credentialsId: '6b8c6026-3bad-4bc5-8a3a-d10da69698bd',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )
        ]) {
            sh '''
                echo "$DOCKER_PASS" | docker login \
                -u "$DOCKER_USER" \
                --password-stdin
            '''
        }
    }
}
        stage('docker tag'){
            steps{
                sh '''
                docker tag ${IMAGE} ${IMAGE}:${BUILD_NUMBER}
                '''
            }
        }
        stage('docker push'){
            steps{
                sh '''
                docker push ${IMAGE}:${BUILD_NUMBER}
                '''
            }
        }
        stage('run app'){
            steps{
                sh '''
                docker stop dev-app
                docker rm dev-app
                docker run -d -p 5000:8081 --name dev-app ${IMAGE}
                '''
                
            }
        }
        stage('logs'){
            steps{
                sh '''
                docker logs dev-app
                '''
            }
        }
        stage('helth check'){
            steps{
                sh '''
                sleep 5
                curl http://172.17.0.3:5000
                '''
            }
            
        }
        
        
    }
    post {

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the Console Output.'
        }

        always {
            echo "Build Number: ${BUILD_NUMBER}"
        }
    }
}
