#!/bin/bash
docker run -d --net collector-net --ip 172.18.0.4 \
	-v db:/data/db \
	--name collector-mongo \
	-p 27017:27017 \
	mvertes/alpine-mongo
