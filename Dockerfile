FROM python:3

RUN pip install redis
RUN pip install bottle

COPY cache_http.py /
EXPOSE 65432

ENTRYPOINT ["python", "cache_http.py"]