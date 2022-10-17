pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = "dilipnigam007"
        APP_NAME = "gitops-demo"
        IMAGE_TAG = "${BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}" + "/" + "${APP_NAME}"
        REGISTRY_CREDS = 'dockerhub'
        }

    stages {
        stage('Build') {
            steps {
                sh "echo hi && echo ${BUILD_NUMBER} && cd /var/lib/jenkins/workspace/pipeline && docker build -t ${IMAGE_NAME}:latest ." 
                
            }
        }
        stage('Push Docker Image'){
            steps {
                 withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable:   'password',usernameVariable:'user')]) {
                     sh "docker login -u $user --password $password"
                     sh "docker push ${IMAGE_NAME}:latest"
                     
                     
                 }
            }
        }

        
    
        
        
    }
}