st_api:
	python3  api/api.py 

st_rb:
	docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-managementdocker run -d -p 5672:5672 -p 15672:15672 -p 25672:25672 -p 4369:4369 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management	
	




