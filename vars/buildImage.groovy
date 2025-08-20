def call(String name, String tag, String fileId){
    configFileProvider([configFile(fileId: fileId, variable: 'env')]) {
        sh "docker build --env-file $env -t ${name}:${tag} ."
    }
}