FROM ubuntu AS compile-image

WORKDIR /app/

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

RUN python3 -m venv venv

ENV PATH="/app/venv/bin:$PATH"

COPY . .

RUN pip install -r requirements.txt

RUN pip install .


FROM  python:3.12-slim

WORKDIR /app/

COPY --from=compile-image /app/venv /app/venv

COPY --from=compile-image app/entrypoint.py /app

ENV PATH="/app/venv/bin:$PATH"

EXPOSE 8501

CMD ["python","entrypoint.py"]