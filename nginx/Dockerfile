FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
COPY flask_conf /etc/nginx/sites-enabled/
RUN usermod -u root
ADD /vagrant/web/ /static/
