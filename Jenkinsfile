node {

    environment {
        access_key = 'TXOT63BC22BONR%6X'
        secret_key = 'xxxxxxxxxxxxxxspdzNG0Aaa21dSd5yyyyyyyyy'
        aws_token = '64565757CXVzLXdlc3QtMiJIMEYCIQCX8sQ4zJ/oBCJ3o76576576576DMXPIZEUwIhAI7xhyxHyGfD8HrNt76765765765BtbZ5NRKqQDCH765765gyNTM4MjU2MDUyIgx73lASMiiBGnZ5ls8qgQOsVWohG9aIQNZ84td29r7hOjJxW1OSeIritNBmEw+roumeUB6JW7MW/BGnS+KuHnpZ5qR/Wuc9Mebs6kRo4usMHdy5cXHVvzumhI37JFyRUR1r3NkdTJhFtX3idpD7V+jdA1AskDYK5/N3NcVhhjnZW7rh4ghAWDuM6X7b1klBFp+yCoirmmTeQG9pj3DbQjM/qLmdBKuMITQlupWGrRz3TegqxRLsG06ljA96aTuPN/5eMr+uMbXpUhEGQ6qUNBpG6nQvPShPbawfuCGMworSM3cF3CmBiN5Bwpo2CwiLv8jpy81/vTJu0Df+JkRlJYvaeOD+q+WgrvkLSMbkepjGa7iC/dtS48M1Ok0zCTU3in37q88vA/Er5nbJ1o4oLTeTDmzYGjE8XEmyLgOCgjXYj49bG1C9DXBiGtlwxP5RQ590FWE8bdENRgyWkC9hSKC+WqPY83vU9z9WaXf0tRUgGym+JiMhtf7KI34BsrIU+50FPQnBeBEsOHrsfZhcA+dcMOv4up0GOqUBlveiprP1B+44qwBRenpUx1q1MWBD9g/QnAtXfDHf1Wx8M5FyalcO/J9M/oSiVl4w+OiWdb+w21aOyjD4E/+n6U3pwVi3crxBovZ6QqyyRceyzUb1iuI4kR9kxHbO6ihnWgOgwlVCyNVY4F1ysUA6BbdiW/gPsQhkNB7SHJX0ch765765765'       
    }

    stage('Preparation') {
        echo "Preparation , if any"
        checkout scm
    }
    
    stage('Confirming Versions') {
        echo "Confirmning Versions"
        // sh 'packer --version'
        // sh 'ansible --version'
        // sh 'terraform -v'
        // sh 'docker --version'
    }
    
    
    
    stage('Creating Docker Image') {
        echo "Creating Docker Image"
        sh 'docker login 76765767.azurecr.io --username 76576576 --password f=756765765765/P8'
        // sh 'docker build --no-cache -t 7657676.azurecr.io/765765765:v1 -f application/Dockerfile application/'        
//         sh 'docker build --no-cache -t 67765765:v1 .'
    }
    stage('Vulnerability Scanning of Image') {
        echo "Vulnerability Scanning of Image"
//         sh 'curl -k -u 7657:767657 --output ./twistcli https://192.168.100.6:8083/api/v1/util/twistcli'
//         sh 'chmod a+x ./twistcli'
//         sh "./twistcli images scan --u 675765 --p 67676 --address https://192.168.100.6:8083/ --docker-address https://docker:2376 --docker-tlscacert /certs/client/ca.pem --docker-tlscert /certs/client/cert.pem --docker-tlskey /certs/client/key.pem allinoneazimages1.azurecr.io/log4jvulnserver10:v1"
    }
    stage('Publish The Docker Image to Registry') {
        echo "Publish The Docker Image to Registry"
//         input("Do you want to proceed")
//         sh 'docker push 7657657657.azurecr.io/765765765:v1' 
    }

    stage('Build Base Image with Docker') {
         echo "Build Base Image with Docker"
        //  sh 'packer --version'
        //  sh 'packer validate buildbaseimage.json'
        //  sh 'packer build buildbaseimage.json'

          //Pull Image in k8s env
         }
     stage('Create Instance from base image') {
         echo "Create Instance from base image"
        //  sh 'terraform init'
        //  sh 'terraform -v'
        //  sh 'terraform validate'
//          sh 'terraform apply -auto-approve'
        //  sh 'terraform destroy -auto-approve'
        // sh  """
        //     terraform init; terraform plan; -var 'access_key=$access_key' -var 'secret_key=$secret_key' -var 'token=$aws_token'
        //     """        
         }        

    stage('Testing Login to instance'){
        sshagent(credentials: ['sshtoinstance'])
         {
            sh '''
                ssh 765767@18.183.255.789 /bin/bash << EOF
                docker ps
                docker images
                docker login retretrret.azurecr.io --username trrtrtr --password f=trtrtretrtr/P8
                docker pull rtretretet.azurecr.io/log4jvulnserver10:v1
                docker run --name vuln1  -d -p 98:8080 rtretretretre.azurecr.io/trtrtr:v1
                exit
                #curl localhost:98/httpheaderua
                EOF
            '''
        }
    }
 


    
    stage('Pull Image in k8s env') {
         echo "Pull Image in k8s env"
          //Pull Image in k8s env
         }

    stage('Run image') {
         // Run Image in k8s env
         echo "Run Image in k8s env"
         }  

}
