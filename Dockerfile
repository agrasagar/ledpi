FROM balenalib/rpi-raspbian:latest
RUN mkdir -p /usr/docker_ledpi4
RUN apt update
RUN apt install git -y
RUN apt install python3-pip python3-setuptools python3-wheel -qy --no-install-recommends
RUN cd /usr/docker_ledpi4/
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install --no-cache-dir rpi.gpio
RUN cd /usr/docker_ledpi4/;git clone https://github.com/agrasagar/ledpi4.git
RUN cd /usr/docker_ledpi4/ledpi4
WORKDIR /usr/docker_ledpi4/ledpi4
EXPOSE 6994/tcp
ENV NAME ledpi4
RUN export TERM=xterm
ENTRYPOINT ["python3", "app.py", "-p", "6994"]

