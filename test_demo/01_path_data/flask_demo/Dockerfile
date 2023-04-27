FROM python:3.9.5-slim
COPY test.py ../flask_demo/test.py

RUN pip install flask -i  https://pypi.tuna.tsinghua.edu.cn/simple/

WORKDIR /src
ENV FLASK_APP=app.py

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]