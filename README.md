■ Prerequisites
	- Single node Kubernetes cluster was deployed using K3s
	- Docker engine installation
■ Setup instructions
	- MySQL DB cluster
		- Created new directory to place DB files /root/kube_definitions/old_versions
		- Created new namespace named 'db'
		- Created four Kubernetes definition files
			- mysql-secret.yaml 	--> DB Credentials
			- mysql-service.yaml	--> NodePort Service 
			- mysql-persistentvolclaim.yaml	--> DB Persistent Volume
			- mysql-statefulset.yaml	--> DB Cluster
	- REST API
		- Created new directory to place REST API files /root/RestAPI
		- Created new namespace named 'web'
		- Created four Kubernetes definition files
			- main.py		--> Python API Service
			- requirements.txt	--> API Requirements
			- Dockerfile 		--> RestAPI Dockerfile
			- deployment.yaml	--> Kubernetes Deployment
			- service.yaml		--> REST API Service		
■ How to test the API
	
	curl -X POST http://10.43.52.126:80/log-ip
	{"message":"IP logged 		successfully","entry":{"ip":"10.42.0.1","timestamp":"2025-08-19T16:41:54.	143350"}}
■ Any limitations or considerations
	- SSH port was not accessible lately
	- Docker Hub site was also not accessible
	- Rest API was initially verified using Curl. Second setup was created to establish connection with DB however, containers show an error. Error messages are also attached. 