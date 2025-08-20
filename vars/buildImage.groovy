def call(String name, String tag, String fileId){
    configFileProvider([configFile(fileId: fileId, variable: 'ENV_FILE')]) {
        sh "docker build --env-file $ENV_FILE -t ${name}:${tag} ."
    }
}