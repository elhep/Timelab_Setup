#!/bin/bash

docker run \
 --name influxdb2-collector \
 --publish 8086:8086 \
 --mount type=volume,source=data,target=/var/lib/influxdb2 \
 --mount type=volume,source=config,target=/etc/influxdb2 \
 --env DOCKER_INFLUXDB_INIT_MODE=setup \
 --env DOCKER_INFLUXDB_INIT_USERNAME=fr_trsQwaJ \
 --env DOCKER_INFLUXDB_INIT_PASSWORD=mf_EI4x4aoB4PVPi \
 --env DOCKER_INFLUXDB_INIT_ORG=isepw \
 --env DOCKER_INFLUXDB_INIT_BUCKET=collector \
 influxdb:2-alpine
