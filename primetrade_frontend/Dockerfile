FROM debian:stable-slim AS build

RUN apt update && apt install -y curl unzip xz-utils git

# Install Flutter
RUN git clone https://github.com/flutter/flutter.git /flutter
ENV PATH="/flutter/bin:${PATH}"
RUN flutter doctor

WORKDIR /app
COPY . .
RUN flutter build web

# Serve via NGINX
FROM nginx:1.27.0-alpine3.20
COPY --from=build /app/build/web /usr/share/nginx/html
EXPOSE 80
