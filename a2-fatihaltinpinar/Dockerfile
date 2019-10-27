# This is a comment!

# Since docker images built upon each other, we need a base image. 
# We use Python image from the main registry. 3 after the column is the label.
# Since I want to run this app on Python 3 I added that label there. 
FROM python:3

# This line copies all the files from the folder where Dockerfile is to
# the given destination in the image.
ADD ./ /webpage/

# This line installs bottle library to image.
# RUN command is used in building the image.
RUN pip install bottle

# I needed root privileges thus I switch to root
USER root

# I export port 8080 since Bottle uses 8080
EXPOSE 8080

# Change working directory
WORKDIR /webpage/

# Start the webserver.
# CMD command runs when the image is deployed.
CMD [ "python" , "./bottle_app.py" ]
