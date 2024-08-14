pipeline {
    agent any
    
    parameters {
        string(name: 'replicas', defaultValue: '4', description: 'set the amount of replicas in deployment')
    }
    
    stages {
    
        stage('Clone Deployment Repo') {
            steps {
                git branch: 'deploy', credentialsId: 'clone-deploy-repo', url: 'http://172.31.35.151/labusers/jenkins-eks-deploy'
            }
        }
        
        stage('Update replicas') {
            steps {
                dir('/home/ec2-user/workspace/eks-replica/chartforecast/templates') {
                    sh 'yq -i ".spec.replicas = $replicas" forecastapp.yaml'
                }
                
            }
        }

        stage('Update image tag') {
            steps {
                dir('/home/ec2-user/workspace/eks-replica/chartforecast') {
                    sh 'TAG=$(curl -s https://registry.hub.docker.com/v2/repositories/oraharon/kube-jenkins-docker/tags/ | jq -r ".results[0].name")'
                    sh "yq -i '.forecastapp.tag=$TAG' values.yaml"
                }
                
            }
        }

        stage('Deploy'){
            steps{
                withAWS(credentials:'jenkins-eks') {
                sh 'aws eks update-kubeconfig --name pc-eks --region eu-north-1'
                dir('/home/ec2-user/workspace/eks-replica/chartforecast') {
                    sh 'helm upgrade chartforecast .'
                    }
                }
            }   
        }

    }
}
