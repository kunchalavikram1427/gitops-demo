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
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Push Docker Image'){
            steps {
                 withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable:   'password',usernameVariable:'user')]) {
                     sh "docker login -u $user --password $password"
                     sh "docker push ${IMAGE_NAME}:latest"
                     
                     sh "ls -lrt"
                     
                     
                 }
            }
        }

        stage('Delete Docker Images'){
            steps {
                sh "docker rmi ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker rmi ${IMAGE_NAME}:latest"
                
            }
        }

        stage('deploy') {

            steps {
                sshagent(['kubeadmin']) {
    
                 sh "ls -lrt"
                 
                 sh "whoami"
                 sh "id"
                 sh "sudo sftp ubuntu@172.31.28.115"
                 sh "sudo sh -x x"
                
                 
                 
                }
                
            }

        }   
             

        
    
        
        
    }
}