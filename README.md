# REST API UI Automation Container with Selenium

## Docker
Docker will expose port 4444 (change as you please). When ready, simply use the Dockerfile to build the image.

```sh
docker-compose build
docker-compose up
```

Once the container is up and running, the selenium_script.py will execute. The default script has goes to python.org and captures a screeenshot