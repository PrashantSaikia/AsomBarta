# AsomBarta

Steps to deploy in GCP:

1. Initialize the gcloud CLI: `gcloud init`
2. Download the repo: git clone https://github.com/PrashantSaikia/AsomBarta.git
3. Create a new Docker repository in Artifact Registry named asom-barta in the location us-west2 with the description "Docker repository": `gcloud artifacts repositories create asom-barta-image --repository-format=docker --location=us-west2 --description="Docker repository"`
4. Verify that your repository was created: `gcloud artifacts repositories list`. You will see `asom-barta` in the list of displayed repositories.
5. Get your Google Cloud project ID by running the following command: `gcloud config get-value project`
6. Build an image using Dockerfile by running the following command from the directory containing quickstart.sh and Dockerfile: `gcloud builds submit --region=us-west2 --tag us-west2-docker.pkg.dev/project-id/asom-barta/asom-barta-image:tag1`.

You will see something like this at the end:
'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ID: 588a0cf7-b115-4fe1-b235-7b30683da64d
CREATE_TIME: 2023-05-23T07:07:59+00:00
DURATION: 30M8S
SOURCE: gs://asom-barta-qna-bot_cloudbuild/source/1684825675.528156-1ca5dee0f1b14f0bafd8aba66e340da9.tgz
IMAGES: us-west2-docker.pkg.dev/asom-barta-qna-bot/asom-barta/asom-barta-image:tag1
STATUS: SUCCESS
'''
8. Configure Docker to use your Artifact Registry credentials when interacting with Artifact Registry. (You are only required to do this once.) Use the following command to authenticate using the gcloud credential helper: `gcloud auth configure-docker HOSTNAME-LIST`

In our case, `gcloud auth configure-docker us-west2-docker.pkg.dev`

9. Run the Docker image that you built before:

`docker run LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME`

where:

LOCATION: the regional or multi-regional location for your repository.
PROJECT_ID: your Google Cloud project ID.
REPOSITORY: the name of your Artifact Registry repository.
IMAGE_NAME: the name of your container image.

In our case, `docker run us-west2-docker.pkg.dev/asom-barta-qna-bot/asom-barta/asom-barta-image:tag1`
