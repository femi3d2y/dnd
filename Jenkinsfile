pipeline{
	agent any

	stages{
		
		
        	stage('--docker-compose build and push--'){
			steps{
                    		sh '''ssh -t jenkins@project-app  << IFE
				cd project/dnd
				sudo git pull
                           	docker-compose build 
                           	docker-compose push
				
                           	'''
            
            		}
        	}
		stage('--Replicate services--'){
			steps{
				sh '''ssh -t jenkins@project-app  << IFE
                       		cd project/dnd
				docker service update --replicas 3 dnd_flask-app
				docker service update --replicas 2 dnd_flask-service
				docker service update --replicas 2 dnd_flask-service2
				docker service update --replicas 2 dnd_flask-data
				
				'''
			}
		}
		stage('--Update service--'){
			steps{
				sh '''ssh -t jenkins@project-app  << IFE
                       		cd project/dnd
				docker service update --image 35.234.154.83:5000/stackapp:${BUILD_NUMBER} dnd_flask-app
				
				
				'''
			}
		}
	}
}
