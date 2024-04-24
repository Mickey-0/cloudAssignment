FROM python:3.12.2
WORKDIR /app
COPY . /app
RUN pip install nltk
RUN python -m nltk.downloader stopwords
CMD ["python", "stopWords.py"]
