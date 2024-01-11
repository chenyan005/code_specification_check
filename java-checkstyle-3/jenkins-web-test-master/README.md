# jenkins-web-test

# Build
mvn clean package && docker build -t blog.elmland/jenkins-web-test .

# RUN

docker rm -f jenkins-web-test || true && docker run -d -p 8080:8080 -p 4848:4848 --name jenkins-web-test blog.elmland/jenkins-web-test 

# Test

curl --location --request GET 'http://localhost:8080/jenkins-web-test-1.0.0-SNAPSHOT/v1/echo' --header 'Content-Type: application/json'