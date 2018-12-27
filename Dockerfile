FROM  python:3.6
MAINTAINER Daniel Gisolfi
RUN apt-get update

# Set the TimeZone 
RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime
RUN dpkg-reconfigure tzdata

WORKDIR /SMSBot
COPY ./src .
COPY ./requirements.txt .

# SET ALL ENVIORMENT VARIABLES
ENV account_sid=ACa0d22c02571056163c578e25396cb680
ENV auth_token=5d87c2611f40b90211ecd7ec6fc8c7aa
ENV account_num=+18458672441
ENV target_num=+18452402529‬

RUN pip install -r requirements.txt
CMD ["python","-u","Bot.py"]