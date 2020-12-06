# start from a php container including apache
FROM php:7.0-apache

# move contents of src/ to /var/www/html in containter
COPY src/ /var/www/html

# listen on port 80
EXPOSE 80

# to build image:
# docker -t hello-world .
#   -t --tag    give it a name

# to instantiate container from image:
# docker run -p 80:80 hello-world
#   -p x:y      forward host port x to container port y
