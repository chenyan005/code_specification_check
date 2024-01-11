#!/bin/sh
sh gradlew clean assemble && docker build -t blog.elmland/jenkins-web-test .
docker rm -f jenkins-web-test || true && docker run -d -p 8080:8080 -p 9990:9990 --name jenkins-web-test -it blog.elmland/jenkins-web-test
