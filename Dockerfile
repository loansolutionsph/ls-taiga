FROM benhutchins/taiga
MAINTAINER Benjamin Hutchins <ben@hutchins.co>

# Install additional extensions
RUN pip install taiga-contrib-slack

COPY slack.js /usr/src/taiga-front-dist/dist/js/slack.js

# Copy SSL Certificates
COPY ssl/ssl.key /etc/nginx/ssl/ssl.key
COPY ssl/ssl.crt /etc/nginx/ssl/ssl.crt

COPY taiga-conf/local.py /taiga/local.py
COPY taiga-conf/conf.json /taiga/conf.json
