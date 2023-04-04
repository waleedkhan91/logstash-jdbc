This is a PoC for logstash to read logs from Microsoft SQL Database table continuously.

To generate elastic documents from logstash interactively from CLI, run logstash container with following command:

    sudo docker run -it --rm logstash:7.7.1 -e 'input { stdin { } } output { elasticsearch { hosts => ["http://<elastic-ip>:9200"] index => "basic-%{+YYYY.MM.dd}" document_type => "test_logs" user     => "elastic" password => "changeme" } stdout { codec => rubydebug } }'

This PoC shows we can get data from MSSQL table and ingest it in elasticsearch. Run the docker-compose in following sequence:

    docker-compose-ek.yaml -> This will start Elasticsearch and kibana containers.

    docker-compose-db.yaml -> This will start MSSQL database container.

    docker-compose-ingestion.yaml -> This will start ingesting random data 

    docker-compose-logstash.yaml -> This will start logstash instance and initiate pipeline.
