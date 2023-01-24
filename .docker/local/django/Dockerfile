ARG PYTHON_VERSION=3.11-slim-bullseye

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  libpq-dev \
  gettext \
  curl \
  gnupg \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Install node
# RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
#     curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
#     echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
#     apt-get update && \
#     apt-get install -qq -y nodejs yarn && \
#     rm -rf /var/lib/apt/lists/*

WORKDIR /app
