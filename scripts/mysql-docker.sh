#/bin/bash

docker start jogoteca > /dev/null

if [ $? -eq 1 ]; then
	echo "Esse container não existe, criando .."
	docker run -p 3306:3306 --name jogoteca -e MYSQL_ROOT_PASSWORD=root -v jogoteca:/var/lib/mysql -d mysql
else
	echo "Esse container já esta rodando"
fi

