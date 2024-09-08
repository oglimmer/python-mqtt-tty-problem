FROM python

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x bridge.py

# CMD ["python", "-u", "bridge.py"]
CMD ["python", "bridge.py"]
