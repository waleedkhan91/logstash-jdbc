ARG ELK_VERSION

# https://www.docker.elastic.co/
FROM docker.elastic.co/logstash/logstash:${ELK_VERSION}

COPY mssql-jdbc-12.2.0.jre11.jar /usr/share/logstash/logstash-core/lib/jars/mssql-jdbc-12.2.0.jre11.jar

USER root
RUN chown logstash:root /usr/share/logstash/logstash-core/lib/jars/mssql-jdbc-12.2.0.jre11.jar
USER logstash