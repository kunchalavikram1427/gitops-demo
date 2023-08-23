pipeline {
    agent any

    stages{
        stage("Checkout SCM"){
            steps{
                script{
                    sh "echo Checkout SCM"
                }
            }
        }
        stage("Create Build"){
            steps{
                script{
                   sh "echo Create Build"
                }
            }
        }
        stage("Create Image"){
            steps{
                script{
                   sh "echo Create Image"
                }
            }
        }
        stage("Push Image to Docker"){
            steps{
                script{
                   sh "echo Push Image to Docker"
                }
            }
        }
    }
}