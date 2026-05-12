pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar-token')
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'YOUR_GITHUB_REPO_LINK'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                sh '''
                sonar-scanner \
                -Dsonar.projectKey=YOUR_PROJECT_KEY \
                -Dsonar.organization=YOUR_ORG \
                -Dsonar.sources=. \
                -Dsonar.token=$SONAR_TOKEN
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t bad-ml-project .'
            }
        }

    }
}
