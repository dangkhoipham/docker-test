FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install flask==1.1.1 && pip3 install requests==2.22.0
COPY test_authen.py /files/test_authen.py
RUN mkdir /logs
WORKDIR /files
ENV LOG "1"
CMD ["python3", "/files/test_authen.py"]
