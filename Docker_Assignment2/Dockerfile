FROM alpine
RUN apk add --no-cache python3
ADD  /main.py /home/main.py
ADD /Limerick.txt /home/data/Limerick.txt
ADD /IF.txt /home/data/IF.txt
RUN mkdir -p /home/output/
CMD  ["/home/main.py"]
ENTRYPOINT  ["python3"]