def APP_NAME = 'prime-session'
def TAG_NAMES = ['dev', 'test', 'prod']
def TAG_NAMES_BACKUP = ['devbackup', 'testbackup', 'prodbackup']
def BUILD_CONFIG = APP_NAME
def IMAGESTREAM_NAME = APP_NAME
def EMAILS = 'jam.hamidi@maximusbc.ca'

// def result = 0;
//
// node('python') {
//     stage('Unit Test') {
//         checkout scm
//         try {
//             sh 'pip install --upgrade pip && pip install -r requirements.txt'
//             sh 'export PYTHONPATH=./venv/lib/python2.7/site-packages && coverage erase && coverage run --source=. manage.py test && coverage html && coverage xml'
//         } catch(Throwable t) {
//             result = 1;
//             mail (from: "EMAIL_FROM", to: EMAILS, subject: "FYI: Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) unit test failed", body: "See ${env.BUILD_URL} for details. ");
//         } finally {
//             if(fileExists('htmlcov/index.html')) {
//                 publishHTML (target: [
//                     allowMissing: true,
//                     alwaysLinkToLastBuild: true,
//                     keepAll: true,
//                     reportDir: 'htmlcov',
//                     reportFiles: 'index.html',
//                     reportName: "Unit Test Code Coverage Report" ])
//             }
//         }
//     }
// }
//         
// echo "result is ${result}"
// if (result != 0) {
//     echo "[FAILURE] Unit Test stage failed"
//     currentBuild.result = 'FAILURE'
//     return
// }
 
node {
    
    stage('build ' + BUILD_CONFIG) {
        openshiftBuild bldCfg: BUILD_CONFIG, showBuildLogs: 'true'
        echo ">> Getting Image Hash"
        IMAGE_HASH = sh (
            script: """oc get istag ${IMAGESTREAM_NAME}:latest -o template --template=\"{{.image.dockerImageReference}}\"|awk -F \":\" \'{print \$3}\'""",
 	    returnStdout: true).trim()
        echo ">> IMAGE_HASH: $IMAGE_HASH"
    }

    stage('deploy-' + TAG_NAMES[0]) {
        echo "Deploying to: " + TAG_NAMES[0]
        // new tag
        openshiftTag destStream: IMAGESTREAM_NAME, verbose: 'true', destTag: TAG_NAMES[0], srcStream: IMAGESTREAM_NAME, srcTag: "${IMAGE_HASH}"
    }
}

node {

    stage('deploy-' + TAG_NAMES[1]) {
        input "Deploy to " + TAG_NAMES[1] + "?"
        echo "Deploy to " + TAG_NAMES[1] + " " + IMAGESTREAM_NAME + ":" + "${IMAGE_HASH}"
        openshiftTag destStream: IMAGESTREAM_NAME, verbose: 'true', destTag: TAG_NAMES_BACKUP[1], srcStream: IMAGESTREAM_NAME, srcTag: TAG_NAMES[1]
        openshiftTag destStream: IMAGESTREAM_NAME, verbose: 'true', destTag: TAG_NAMES[1], srcStream: IMAGESTREAM_NAME, srcTag: "${IMAGE_HASH}"
    }
}

node {

    stage('deploy-'  + TAG_NAMES[2]) {
      input "Deploy to " + TAG_NAMES[2] + "?"
      echo "Deploy to " + TAG_NAMES[2] + " " + IMAGESTREAM_NAME + ":" + "${IMAGE_HASH}"
      openshiftTag destStream: IMAGESTREAM_NAME, verbose: 'true', destTag: TAG_NAMES_BACKUP[2], srcStream: IMAGESTREAM_NAME, srcTag: TAG_NAMES[2]
      openshiftTag destStream: IMAGESTREAM_NAME, verbose: 'true', destTag: TAG_NAMES[2], srcStream: IMAGESTREAM_NAME, srcTag: "${IMAGE_HASH}"
   }
}
