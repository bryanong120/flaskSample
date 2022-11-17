def NETWORK = UUID.randomUUID().toString()
def CHROME_CONTAINER = "chrome-${NETWORK}"
def APP_CONTAINER = "app-${NETWORK}"

pipeline {
  agent none

  environment {
    WEBDRIVER_HOST = "${CHROME_CONTAINER}"
    APP_URL = "http://${APP_CONTAINER}:3000"
  }

  stages {
    stage('Bootstrap services') {
      agent any
      steps {
        script {
          sh "docker network create ${NETWORK} || true"
          CHROME = docker.image('seleniarm/standalone-chromium:latest').run("--name ${CHROME_CONTAINER} --network ${NETWORK} --shm-size=2g")
        }
      }
    }

    stage('Build and Test') {
      agent {
        docker {
            image 'python:3.10'
            args "-u root --network ${NETWORK} --name ${APP_CONTAINER}"
        }
      }

      steps {
        sh 'pip install -r requirements.txt'
        sh 'python app.py &'
        sh "pytest --driver Remote --selenium-host ${WEBDRIVER_HOST} --selenium-port 4444 --capability browserName chrome"
      }
    }

  }
  post {
    always {
      node(null) {
        script {
          if (CHROME) {
            CHROME.stop()
          }

          sh "docker network rm ${NETWORK} || true"
        }
      }
    }
  }
}
