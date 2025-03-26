FROM python:3.11
WORKDIR /app
COPY chatbot.py /app
COPY requirements.txt /app
COPY ChatGPT_HKBU.py /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python chatbot.py