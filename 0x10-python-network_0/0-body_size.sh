#!/bin/bash
# Outputs the size of the content fetched from the given URL
curl -s "$1" | wc -c