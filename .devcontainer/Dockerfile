# Copyright © 2001 by the Rectors and Visitors of the University of Virginia. 

# Extend Ubunto 18.04 (As of 10/22 there seem to be missing libs needed by Dafny in 20.04)

FROM python:3.11-slim-bookworm

# Create image without any user interaction
ENV DEBIAN_FRONTEND=noninteractive
ARG DEBCONF_NOWARNINGS="yes"
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

SHELL ["/bin/bash", "-c"]

# Update and configure Ubuntu 
RUN apt-get clean && apt-get update -y && apt-get upgrade -y && apt-get update --fix-missing
RUN apt-get install -y locales && locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 

# Shouldn't need this but ...
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen

# Install essential tools and libraries
RUN apt-get -y install lsb-release build-essential git vim wget gnupg curl unzip libssl-dev libffi-dev libconfig-dev 

# Get dotnet -- doesn't work, package not yet available for Debian 12
# RUN apt-get update && \
#  apt-get install -y dotnet-sdk-7.0

# Perform following actions in containers /root directory
WORKDIR /root 

# Set up bash .profile
COPY .profile.txt /root/.profile

#RUN adduser --disabled-password --comment localuser
#USER localuser

RUN python -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pip

RUN apt-get -y install python3-tk

