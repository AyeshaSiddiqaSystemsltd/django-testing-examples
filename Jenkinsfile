pipeline {
  agent any
  stages {
    stage('Buzz buzz') {
      steps {
        echo 'Bees Buzz!'
        sh 'echo Edited Placeholder'
      }
    }

    stage('beesbees') {
      parallel {
        stage('beesbees') {
          steps {
            echo 'HelloWorld!'
            sh 'sleep 10'
          }
        }

        stage('Buzz') {
          steps {
            echo 'Myworldismine'
            sh 'echo Success!'
          }
        }

        stage('Buzz Test') {
          steps {
            echo 'dwsw'
          }
        }

      }
    }

    stage('Buzz Test') {
      steps {
        echo 'hola'
      }
    }

  }
}