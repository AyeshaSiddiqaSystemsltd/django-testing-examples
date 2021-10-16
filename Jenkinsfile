pipeline {
  agent any
  stages {
    stage('Buzz buzz') {
      steps {
        echo 'Bees Buzz!'
      }
    }

    stage('beesbees') {
      parallel {
        stage('beesbees') {
          steps {
            echo 'HelloWorld'
          }
        }

        stage('Buzz') {
          steps {
            echo 'Myworldismine'
          }
        }

      }
    }

  }
}