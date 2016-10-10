FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
COPY flask_conf /etc/nginx/sites-enabled/
RUN adduser nginx && usermod -u 1000 nginx
ADD /vagrant/web/ /static/
COPY /vagrant/web /static
