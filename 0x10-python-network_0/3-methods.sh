#!/bin/bash
#displays all methods on the server
curl -X OPTIONS -w "\n" "$1"
