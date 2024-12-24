# Use a base image that has Python and necessary dependencies
FROM python:3.9-slim

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium-driver \
    chromium \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    fonts-liberation \
    libnspr4 \
    libnss3 \
    libxtst6 \
    libx11-xcb1 \
    libgbm-dev \
    libxshmfence1 \
    ca-certificates

# Install Python dependencies (Selenium)
RUN pip install selenium

# Set environment variables for headless Chromium
ENV DISPLAY=:99
ENV CHROME_BIN=/usr/bin/chromium

# Copy your Python script into the container
COPY selenium_script.py /app/selenium_script.py

# Command to run the script
CMD ["python", "/app/selenium_script.py"]
