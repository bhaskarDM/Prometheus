from tiangolo/uwsgi-nginx-flask:python3.8
run pip install prometheus_client
ENV LISTEN_PORT 5001
Expose 5001
copy ./app /app
workdir /app