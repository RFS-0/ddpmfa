DDPMFA
======

Installation
------------

1) If you haven't already, install [Docker](https://www.docker.com/). Docker is available for [many platforms](https://docs.docker.com/engine/installation/), e.g.:
   - [Docker for Windows 10 Pro](https://www.docker.com/docker-windows)
   - [Docker for other Windows versions (e.g. Windows 10 Home, Windows 7 etc.)](https://docs.docker.com/toolbox/toolbox_install_windows/)
   - [Docker for Mac](https://www.docker.com/docker-mac)
   - Ubuntu: `sudo apt-get install docker.io`

2) 	If you use Docker for Windows, Docker for Mac or Linux you can pull the Docker image by entering the following command into your system console:
   
   ```
   docker pull aurum79/ddpmfa:latest
   ```
   
   Note: On Windows you have to switch to linux containers. Refer to (https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) for details on how to do this.
   
   If you use Docker Toolbox for Windows you have first to open the [Docker Quickstart Terminal] (https://docs.docker.com/toolbox/toolbox_install_windows/#step-3-verify-your-installation) and then you can pull the Docker image by entering the following command into your the [Docker Quickstart Terminal](https://docs.docker.com/toolbox/toolbox_install_windows/#step-3-verify-your-installation):
   
   ```
   docker pull aurum79/ddpmfa:latest
   ```
   	
   
3)	If you use Docker for Windows, Docker for Mac or Linux you can start the container by entering the following command into your system console:
   
   ```
   docker run -d -p 8001:8000 --restart unless-stopped aurum79/ddpmfa:latest
   ```
   
   If you use Docker Toolbox for Windows  you can start container by entering the following command into the Docker Quickstart Terminal:
   ```
   docker run -d -p 8001:8000 --restart unless-stopped aurum79/ddpmfa:latest
   ```
  
   
4) If you use Docker for Windows, Docker for Mac or Linux: open your browser and enter
   
   ```
   http://127.0.0.1:8001/dpmfa/
   ```
   
   If you use Docker Toolbox for Windows, then you have to go to the ip address of the default machine that docker uses. This ip address is mentioned when the docker quickstart terminal is startet and should be similar to: "docker is configured to use the default machine with IP 192.168.99.100". If you do not change the defaults you should be able to access the app by typing the following into your browser:
   
   ```
   http://192.168.99.100:8001/dpmfa/
   ```
   
5) Restarting the App:
	
	As long as you do not stop the docker container you can re-open the app by just repeating step 4) i.e. by opening the browser and 	going to the ip address you used last time. 
	
	Note: It is important to notice that you should not remove the docker container as long as you need the data stored inside the 	container. If you do remove the container all data will be removed as well.
