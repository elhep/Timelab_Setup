#!/bin/bash

docker run --rm -p 9090:9090 --net collector-net --ip 172.18.0.2 --name collector-api-flask collector-api-flask
