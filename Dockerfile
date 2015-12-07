FROM benhutchins/taiga
MAINTAINER Benjamin Hutchins <ben@hutchins.co>

# Install additional extensions
RUN pip install taiga-contrib-slack

RUN wget "https://raw.githubusercontent.com/taigaio/taiga-contrib-slack/$(pip show taiga-contrib-slack | awk '/^Version: /{print $2}')/front/dist/slack.js"

COPY slack.js /usr/src/taiga-front-dist/dist/js/slack.js

COPY taiga-conf/local.py /taiga/local.py
COPY taiga-conf/conf.json /taiga/conf.json
