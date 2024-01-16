FROM ubuntu:14.04
RUN apt-get update -y
RUN apt-get install -y apache2
COPY index.html /var/www/html/
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
