def call(String name, String tag){
    sh "docker build --network=host -t ${name}:${tag} ."
}