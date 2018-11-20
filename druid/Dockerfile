FROM fokkodriesprong/docker-druid
RUN apt-get update &&\
    apt-get install -y curl &&\
    rm -rf rm -rf /var/lib/apt/lists/*

WORKDIR /srv/app
COPY supervisor-spec.json .
#CMD ["curl","-X","POST","H","Content-Type: application/json","-d","@supervisor-spec.json","http://localhost:8090/druid/indexer/v1/supervisor"]

