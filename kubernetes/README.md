# REST API UI Automation Container with Selenium
> Note: `ocli`  and `kubectl` is required to be configured

Ensure cluster is up
`kubectl cluster-info`

## Deploying Selenium
first step is to bring up the selenium hub
`kubectl create -f selenium-hub-deployment.yaml `

next create a service that the hub can use to communicate
`kubectl create -f selenium-hub-svc.yaml`

next let's create a worker nodes
`kubectl create -f selenium-node-firefox-deployment.yaml `

If you prefer chrome you can create a chrome worker node, just be sure your selenium options are set to the correct browser
`kubectl create --filename=staging/selenium/selenium-node-chrome-deployment.yaml`

## Deploying the application
Ensure the application is uploaded to your OCIR registry

Pre-requisite:
- Auth token ( to create one go to Identity -> Domains -> Default domain -> Users -> (select a user) -> Auth tokens

Steps
- In the OCI console go to OCIR - > Registry -> create repository
- Log into OCIR
  - `docker login <region-code>.ocir.io <tenancy_namespace>/<username> <Auth-token>`
- Find the image in your local machine and tag it in the format
  - `docker images`
  - `docker tag <docker image id> <region-code>.ocir.io/<tenancy-namespace>/<repos-name>/<image-name>:<tag>`
- Push your tagged image to OCIR
  - `docker push iad.ocir.io/username/repo-name/image-name`

Pulling the image
- Note: images can also be pulled with
  - `docker pull <region-code>.ocir.io/<tenancy-namespace>/repo-name/image-name:tag`

### Pulling the image from Registry for Kubernetes Deployments

Create Docker registry secret and use Auth token
  - `kubectl create secret docker-registry <secret-name> --docker-server=<region-code>.ocir.io --docker-username='<tenancy-namespace>/<oci-username>' --docker-password='<oci-auth-token' --docker-email='<email-address>'`

This registry secret will be used in the kubernetes deployment of the app

## Deploying the application and service that will enable the application to have an endpoint through a load balancer
kubectl create -f seluvi_deployment.yaml 

## Trouble shooting / changing the python file

To view the logs of the app
`kubectl logs  <podname> seluv`

To log into the container
`kubectl exec -it <podname> -c seluv -- /bin/bash`
