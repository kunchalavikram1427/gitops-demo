pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = "dilipnigam007"
        APP_NAME = "gitops-demo"
        IMAGE_TAG = "${BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}" + "/" + "${APP_NAME}"
        REGISTRY_CREDS = 'dockerhub'
        DOCKER_TAG = getDockerTag()
        }

    stages {
        stage('Build') {
            steps {
                sh "echo hi && echo ${BUILD_NUMBER} && cd /var/lib/jenkins/workspace/pipeline && docker build -t ${IMAGE_NAME}:latest ." 
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Push Docker Image'){
            steps {
                 withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable:   'password',usernameVariable:'user')]) {
                     sh "docker login -u $user --password $password"
                     sh "docker push ${IMAGE_NAME}:latest"
                     sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                     sh "ls -lrt"
                     
                     
                 }
            }
        }
        stage('change tag') {
            steps {
                sh "echo ${DOCKER_TAG}" 
            }
        }

                

        
    
        
        
    }
}