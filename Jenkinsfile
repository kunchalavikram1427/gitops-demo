pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = "siddharth20"
        APP_NAME = "gitops-demo-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}/${APP_NAME}"
        REGISTRY_CREDS = 'dockerhub'
    }
    stages{
        stage("Cleanup Workspace"){
            steps{
                script{
                    cleanWs()
                }
            }
        }
        stage("Chekout SCM"){
            steps{
                script{
                   git credentialsId: 'gitcred', 
                   url: 'https://github.com/siddharth201983/gitops-demo.git', 
                   branch: 'master'
                }
            }
        }
        stage("Build Docker Image"){
            steps{
                script{
                   docker_image = docker.build "${IMAGE_NAME}"
                }
            }
        }
        stage("Push Image to Docker"){
            steps{
                script{
                   docker.withRegistry('', REGISTRY_CREDS){
                        docker_image.push("${BUILD_NUMBER}")
                        docker_image.push("latest")
                   }
                }
            }
        }
        stage("Delete Docker Images"){
            steps{
                script{
                    sh "docker rmi ${IMAGE_NAME}:${IMAGE_TAG}"
                    sh "docker rmi ${IMAGE_NAME}:latest"
                }
            }
        }
        stage("Update K8s deployment yaml"){
            steps{
                script{
                    sh "cat deployment.yml"
                    sh "sed -i 's/${APP_NAME}.*/${APP_NAME}:${IMAGE_TAG}/g' deployment.yml"
                    sh "cat deployment.yml"
                }
            }
        }
        stage("Push the changed deployment file to git"){
            steps{
                script{
                    sh """
                        git config --global user.name "siddharth201983"
                        git config --global user.email "sharma.siddharth2009@gmail.com"
                        git config pull.ff true
                        git add deployment.yml
                        git commit -m "updated the deployment file"
                    """
                    withCredentials([gitUsernamePassword(credentialsId: 'gitcred', gitToolName: 'Default')]) {
                        sh "git pull https://github.com/siddharth201983/gitops-demo-config.git master --allow-unrelated-histories"
                        sh "git pull https://github.com/siddharth201983/gitops-demo-config.git master"
                    }
                }
            }
        }
    }
}

