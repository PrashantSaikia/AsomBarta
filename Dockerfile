FROM python:3.9

RUN pip install virtualenv && virtualenv venv -p python3
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN git clone https://github.com/facebookresearch/detectron2.git
RUN python -m pip install -e detectron2

# Install dependencies
RUN apt-get update && apt-get install libgl1 -y
RUN pip install -U nltk
RUN [ "python3", "-c", "import nltk; nltk.download('punkt', download_dir='/usr/local/nltk_data')" ]

COPY . /app

# Run the application:
CMD ["python", "-u", "app.py"]