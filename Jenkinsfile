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

    stage('OWASP DependencyCheck') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
			}
		}


    stage('Build and Test') {
      agent {
        docker {
            image 'python:3.8'
            args "-u root --network ${NETWORK} --name ${APP_CONTAINER}"
        }
      }

      steps {
        sh 'pip install -r requirements.txt'
        sh 'python app.py &'
      }
    }

  }
  post {
    always {
      node(null) {
      }
    }
  }
}
