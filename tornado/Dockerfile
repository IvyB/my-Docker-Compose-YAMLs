FROM python:3.7.3 

COPY requirements.txt ./
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -U requests[socks]
EXPOSE 8000
