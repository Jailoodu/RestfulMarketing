FROM python:3

COPY . /api

WORKDIR /api

RUN pip install firebase_admin

RUN pip install flask_restplus

RUN pip install flask

RUN pip install werkzeug

RUN pip install pandas

RUN pip install pytest

RUN pip install pytest-cov

RUN openssl enc -aes-256-cbc -d -in serviceAccountDocker.json.enc -out serviceAccount.json -k mcmasterpw

ENV GOOGLE_APPLICATION_CREDENTIALS="/api/serviceAccount.json"

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]