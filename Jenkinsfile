pipeline{
	agent any

	stages{
		
		
		stage('--Update git repo--'){
			steps{
                    		sh '''su femiadmin
				ssh -t femiadmin@35.246.77.128  << IFE 
                           	sudo apt update
                           	rm -rf project/dnd
                           	cd project/
                           	git clone https://github.com/femi3d2y/dnd.git
                           	cd dnd/
                           	git checkout dev
				
                           	'''
            		}
       	 	}
		
        	stage('--docker-compose build and push--'){
			steps{
                    		sh '''ssh -t femiadmin@35.246.77.128  << IFE
                           	cd project/dnd
                           	docker-compose up -d --build
                           	docker-compose down 
                           	docker-compose push
				
                           	'''
            
            		}
        	}
        	stage('--Deploy services--'){
			steps{
				sh '''ssh -t femiadmin@35.246.77.128  << IFE
                       		cd project/dnd
                       		docker stack deploy docker-compose.yml dnd 
				
				'''
			}
		}
	}
}
