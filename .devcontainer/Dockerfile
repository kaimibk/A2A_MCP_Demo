FROM mcr.microsoft.com/devcontainers/base:ubuntu24.04

# Adding Certs to fix potential ZScaler issues with devcontainer extensions
COPY ./certs/Zscaler-Root-CA.pem /usr/local/share/ca-certificates/Zscaler-Root-CA.crt
RUN cat /usr/local/share/ca-certificates/Zscaler-Root-CA.crt >> /etc/ssl/certs/ca-certificates.crt && \
    update-ca-certificates --fresh
ENV SSL_CERT_DIR=/etc/ssl/certs
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt
