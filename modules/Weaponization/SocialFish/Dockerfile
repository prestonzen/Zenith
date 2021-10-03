FROM python:3
LABEL imageAuthor = "prestonzen@kaizenapps.com"

#copy SocialFish from the root project directory into the container's /opt/SocialFish filepath
COPY . /opt/SocialFish 

#I need to fix the Could not connect to debian.map.fastlydns.net:80 (151.101.26.132). - connect (111: Connection refused) Unable to connect to deb.debian.org:http:
#error when I do a "docker build ." The python packages aren't updating 
#ENV http_proxy http://192.168.29.210:3128
#ENV https_proxy https://192.168.29.210:3128

RUN sed -i "s/httpredir.debian.org/`curl -s -D - http://httpredir.debian.org/demo/debian/ | awk '/^Link:/ { print $2 }' | sed -e 's@<http://\(.*\)/debian/>;@\1@g'`/" /etc/apt/sources.list
RUN apt-get update
RUN apt-get install python3 python3-pip python3-dev -y
WORKDIR /opt/SocialFish
RUN pip install -r requirements.txt 

#RUN pip3 -r requirements.txt

EXPOSE 5000

RUN chmod +x /opt/SocialFish/SocialFish.py

ENTRYPOINT ["/opt/SocialFish/SocialFish.py","root","zenith"]