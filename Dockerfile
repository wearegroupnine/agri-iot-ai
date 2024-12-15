FROM ultralytics/yolov5:latest

WORKDIR ./

COPY requirements.txt ./
RUN apt-get update
RUN apt-get install -y python3.8 python3-pip
RUN apt-get clean
RUN pip3 install flask
RUN pip3 install opencv-python-headless

ADD . ./agri

CMD ["/bin/bash", "./agri/start.sh"]
