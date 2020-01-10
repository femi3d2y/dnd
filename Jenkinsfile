pipeline{
	agent any

	stages{
		stage('--Update git repo--'){
			steps{
                    sh ''' cd /home/femiadmin/ansible/ 
                           sudo apt update
                           ansible-playbook -i inventory git-playbook.yml
                           '''
            }
        }
        stage('--docker-compose push--'){
			steps{
                    sh ''' ansible-playbook -i inventory push.yml
                           '''
            
            }
        }
        stage('--Flask-App started--'){
			steps{
				sh ''' ansible-playbook -i inventory deploy.yml
					'''
			}
		}
	}
}
