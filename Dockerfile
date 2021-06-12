# imports Python 3 base image
FROM python:3 

# sets current directory to /usr/src/app in a debian container
WORKDIR /usr/src/app

# copies requirements.txt file to the container root directory
COPY requirements.txt ./

# installs pip dependencies on image
RUN pip install --no-cache-dir -r requirements.txt

# copies remainding files to the container root directory
COPY . .

# executes python crawler.py on container start
CMD [ "python", "./crawler.py" ]