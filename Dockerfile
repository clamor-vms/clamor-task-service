FROM drone/ca-certs

ADD src/task /

CMD ["/task"]
