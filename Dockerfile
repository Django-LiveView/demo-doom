FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for ViZDoom
RUN apt-get update && apt-get install -y \
	build-essential \
	zlib1g-dev \
	libsdl2-dev \
	libjpeg-dev \
	nasm \
	tar \
	libbz2-dev \
	libgtk2.0-dev \
	cmake \
	git \
	libfluidsynth-dev \
	libgme-dev \
	libopenal-dev \
	timidity \
	libwildmidi-dev \
	libboost-all-dev \
	liblua5.1-dev \
	wget \
	unzip \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose Django port
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
