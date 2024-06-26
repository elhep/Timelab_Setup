#!/bin/bash
docker run \
    -p 8086:8086 \
    -v "$PWD/data:/var/lib/influxdb2" \
    -v "$PWD/config:/etc/influxdb2" \
    --net collector-net --ip 172.18.0.3 \
    influxdb:2-alpine
