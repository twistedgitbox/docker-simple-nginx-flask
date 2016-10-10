FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
COPY flask_conf /etc/nginx/sites-enabled/
RUN adduser nginx && usermod -u 1000 nginx
RUN mkdir -p /usr/share/nginx/html/ && sudo chmod 777 /usr/share/nginx/html/
ADD /vagrant/web/ /static/
COPY /vagrant/web/. /static
COPY /vagrant/web/. /usr/share/nginx/html
RUN sudo chmod 775 -p /usr/share/nginx/html/

CMD ["nginx"]
EXPOSE 80 443

