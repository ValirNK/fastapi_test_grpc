sudo docker-compose -f docker-compose-ci.yaml up -d --build Создаст 3 контейнера с nginx, fastapi, grpc
sudo docker exex -it grpc-docker-container-id bash && python3 grpcapi_client.py db.json Сделает запрос на сохранение из db.json в pysondb (server_db.json) через grpc
Чтобы посмотреть добавленные данные: sudo docker exex -it grpc-docker-container-id bash && cat server_db.json
Сделать запрос на поиск записей в pysondb по article_id: sudo docker exex -it app-docker-container-id bash && python3 aiohttp_client.py -ids [12,123], где ids - список с article_id
Api docs: http://0.0.0.0:8000/docs

Я застрял на volume в докере, у меня не смонтировалась папка с json, поэтому server_db.json обновляется в файловой системе контейнера,
поэтому прописываю sudo docker exex -it grpc bash
