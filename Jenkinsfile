pipeline{
	agent any

	stages{
		
		
        	stage('--docker-compose build and push--'){
			steps{
                    		sh '''ssh -t jenkins@project-app  << IFE
                           	source ~/.bashrc
				export KEY=${KEY}
				export MY_SQL_HOST=${MY_SQL_HOST}
				export MY_SQL_USER = ${MY_SQL_USER} 
				export MY_SQL_PASS = ${MY_SQL_PASS}
				export MY_SQL_DB = ${MY_SQL_DB}
				export MY_SQL_DB_TEST = ${MY_SQL_DB_TEST}
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
