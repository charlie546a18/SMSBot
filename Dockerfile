FROM  python:3.6
MAINTAINER Daniel Gisolfi
RUN apt-get update

# Set the TimeZone 
RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime
RUN dpkg-reconfigure tzdata

WORKDIR /SMSBot
COPY ./src .
COPY ./requirements.txt .

RUN pip install -r requirements.txt
CMD ["python","-u","bot.py"]