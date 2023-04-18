pipeline {
    agent {
        node {
            label 'jenkins-agent-docker'
        }
    }

    environment {

        // GIT_REPOSITORY=''
        // GIT_BRANCH_NAME='main'
        // GIT_CREDENTIALS='GIT_CREDENTIALS'

        // DOCKER_REGISTRY='https://hub.docker.com'
        // DOCKER_REPOSITORY=''
        // DOCKER_CREDENTIALS='DOCKER_CREDENTIALS'

        SERVICE_NAME='notifier'
        VERSION='0.1.0'
    }

    stages {

        // stage('Clone') {
        //     steps {
        //         echo 'Clone...'

        //         // git url: env.GIT_REPOSITORY
        //         // git url: env.GIT_REPOSITORY, branch: env.GIT_BRANCH_NAME
        //         git url: env.GIT_REPOSITORY, branch: env.GIT_BRANCH_NAME, credentialsId: env.GIT_CREDENTIALS
        //     }
        // }

        stage('Build') {

            steps {

                echo "Build ${SERVICE_NAME} on ${VERSION} version..."

                script {
                    dockerImage = docker.build("${DOCKER_REPOSITORY}/${SERVICE_NAME}:${VERSION}")
                }

            }
        }

        stage('Test') {

            when {

                expression {

                    env.BRANCH_NAME == 'dev' || env.BRANCH_NAME == 'staging'
                }
            }

            steps {
                
                echo 'Test...'
            }
        }

        stage('Push') {

            steps {

                echo 'Push...'

                script {
                    docker.withRegistry('', DOCKER_CREDENTIALS) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Remove') {

            steps {
                echo 'Remove...'

                sh "docker rmi ${DOCKER_REPOSITORY}/${SERVICE_NAME}:${VERSION}"
            }
        }
    }
}