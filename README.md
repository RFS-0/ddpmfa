DDPMFA
======

Installation
------------

1) If you haven't already, install [Docker](https://www.docker.com/). Docker is available for [many platforms](https://docs.docker.com/engine/installation/), e.g.:
   
   - [Docker for Windows](https://www.docker.com/docker-windows)
   - [Docker for Mac](https://www.docker.com/docker-mac)
   - Ubuntu: `sudo apt-get install docker.io`

2) Pull the Docker image:
   
   ```
   docker pull aurum79/ddpmfa:latest
   ```
3) Start container:
   
   ```
   docker run -d -p 8001:8000 aurum79/ddpmfa:latest
   ```
4) Open your browser and enter
   
   ```
   http://127.0.0.1:45678/dpmfa/
   ```
