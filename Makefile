create:
	gnome-terminal && docker run -d \
	--name volumenes_db \
	-e POSTGRES_USER=root \
	-e POSTGRES_PASSWORD=root \
	-e POSTGRES_DB=volumenes_db \
	-v volumenes_db:/var/lib/postgresql/data \
	-p 5432:5432 \
	postgres && docker container attach volumenes_db

recreate:
	make stop && make delete && make create

restart: 
	make stop && make connect

connect: 
	gnome-terminal && docker container start volumenes_db && docker container attach volumenes_db

attach:
	docker container exec -it volumenes_db psql -U root

stop: 
	docker container stop volumenes_db
	exit

delete:
	docker container stop volumenes_db && docker container rm volumenes_db

