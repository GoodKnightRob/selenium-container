# REST API UI Automation Container with Selenium

## Docker
Docker will expose port 4444 (change as you please) for the selenium runner and port 8000 for the REST webserver. When ready, simply use the Dockerfile to build the image.

```sh
docker-compose build
docker-compose up
```

Once the container is up and running you can access localhost:8000, which is invoke the selenum script. The default script goes to python.org and captures a screeenshot
