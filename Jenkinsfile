pipeline{
	agent any

	stages{
		
		
        	stage('--docker-compose build and push--'){
			steps{
                    		sh '''ssh -t jenkins@project-app  << IFE
				cd project/dnd
				source ~/.bashrc
				export KEY=${KEY}
				export MY_SQL_HOST=${MY_SQL_HOST}
				export MY_SQL_USER=${MY_SQL_USER} 
				export MY_SQL_PASS=${MY_SQL_PASS}
				export MY_SQL_DB=${MY_SQL_DB}
				export MY_SQL_DB_TEST=${MY_SQL_DB_TEST}
				export BUILD_NUMBER=${BUILD_NUMBER}
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
				docker service update --replicas 4 dnd_flask-app
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
