#!/bin/bash

UID=$(id -u) GID=$(id -g) docker compose up -d --build
