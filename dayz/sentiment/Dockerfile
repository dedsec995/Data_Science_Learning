FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "senti.py"]


# CMD [ "python","senti.py", "I am on of the happiest person on the planet earth"]

# docker run --rm -v model-cache:/root/.cache/huggingface sentiment-app "I am on of the happiest person on the planet earth"

# docker run --rm sentiment-app "I am having a terrible day."