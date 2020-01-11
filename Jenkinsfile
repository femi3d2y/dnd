pipeline{
	agent any

	stages{
		
		
        	stage('--docker-compose build and push--'){
			steps{
                    		sh '''ssh -t -o jenkins@35.246.77.128  << IFE
                           	cd project/dnd
                           	docker-compose up -d --build
                           	docker-compose down 
                           	docker-compose push
				
                           	'''
            
            		}
        	}
        	stage('--Deploy services--'){
			steps{
				sh '''ssh -t -o jenkins@35.246.77.128  << IFE
                       		cd project/dnd
                       		docker stack deploy docker-compose.yml dnd 
				
				'''
			}
		}
	}
}
