def call(String giturl,String gitBranch,String credentialsId){
    git url: "${giturl}"
    branch: "${gitBranch}"
    credentialsId: "${credentialsId}"
}