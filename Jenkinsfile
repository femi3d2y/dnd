pipeline{
	agent any

	stages{
		
		
        	stage('--docker-compose build and push--'){
			steps{
                    		sh '''ssh -t jenkins@project-app  << IFE
                           	source ~/.bashrc
				pwd
				ls
				echo ${MY_SQL_HOST}
				cd project/dnd
                           	docker-compose build 
                           	docker-compose push
				
                           	'''
            
            		}
        	}
        	stage('--Deploy services--'){
			steps{
				sh '''ssh -t jenkins@project-app  << IFE
                       		cd project/dnd
                       		docker stack deploy --compose-file docker-compose.yml dnd 
				
				'''
			}
		}
	}
}
