FROM alpine:latest

RUN apk add --no-cache curl

CMD while true; do \
        curl -s http://web:8080 && echo " -> OK"; \
        sleep 5; \
    done