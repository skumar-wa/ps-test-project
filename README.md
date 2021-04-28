# Creating and deploying an App on Google Cloud Platform
This repository contains source code for building a simple app , provisioning a Google Kubernetes Engine(GKE) Cluster, deploying on it using [Google Cloud Build](https://cloud.google.com/cloud-build/docs/) and configuring auto-scaling and its testing.

## Creating a GKE cluster 
A GKE cluster is created here using [terraform scripts](https://github.com/skumar-wa/ps-test-project/tree/main/Terraform). e2-medium nodes are provisioned in europe-west2 region across its 3 zones.

## Creating sample App
A [sample application](https://github.com/skumar-wa/ps-test-project/tree/main/app) reading contents from [REST endpoint](https://reqres.in/api/products/)
 and displaying to a user is created using python. Associated Dockerfile is provided. Output of application can be accessed [here](http://34.117.4.115/) and looks as below:

![image](https://user-images.githubusercontent.com/83188995/116360003-61881100-a7f7-11eb-8a64-94b735bc868b.png)

## Deploying App on the created GKE cluster
Continuous integration, delivery and deployment are implemented using Google Cloud Build and [Helm 3 charts](https://github.com/skumar-wa/ps-test-project/tree/main/kubernetes).Helm image is built from [cloud builder community repo ](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/helm). Workflow is defined in [Cloud build configuration file](https://github.com/skumar-wa/ps-test-project/blob/main/cloudbuild.yaml). A snapshot of a run is provided below

<img width="625" alt="GitHubCloudBuild" src="https://user-images.githubusercontent.com/83188995/116363186-c5f89f80-a7fa-11eb-9e23-000e83afd036.PNG">

## Auto-scaling and Testing
Auto-scaling for pods is implemented using CPU utilization as a trigger and tested using [JMeter](https://jmeter.apache.org/).
Application pods scale out and in according to the number of HTTP requests generated from JMeter.Few snapshots of testing are provided below

### Before Testing

<img width="781" alt="InitialState" src="https://user-images.githubusercontent.com/83188995/116367772-95673480-a7ff-11eb-8f13-5a698feadc5f.PNG">


### Auto-Scale out during performance testing
Pods scale to 11 with 30 users making 1000 requests

<img width="800" alt="AutoScaleOutFull" src="https://user-images.githubusercontent.com/83188995/116367805-9c8e4280-a7ff-11eb-926b-ee1db25ada0f.PNG">


### Auto-Scale in after tests stopped
Pods scale into 1 ( initial number ) after tests, snapshots is taken during the process when pod replicas dropped to 2

<img width="793" alt="AutoScaleIn" src="https://user-images.githubusercontent.com/83188995/116367832-a2842380-a7ff-11eb-8b13-36a71a642aff.PNG">
