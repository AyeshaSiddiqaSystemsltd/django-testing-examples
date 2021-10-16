pipeline {
  agent any
  stages {
    stage('Buzz buzz') {
      steps {
        echo 'Bees Buzz!'
        sh 'echo Another Placeholder.'
      }
    }

    stage('beesbees') {
      parallel {
        stage('beesbees') {
          steps {
            echo 'HelloWorld'
            sh 'sleep 5'
          }
        }

        stage('Buzz') {
          steps {
            echo 'Myworldismine'
            sh 'echo Success!'
          }
        }

      }
    }

  }
}