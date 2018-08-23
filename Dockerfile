FROM drone/ca-certs

ADD config/config.yaml /etc/skaioskit/config.yaml
ADD src/task /

CMD ["/task"]
