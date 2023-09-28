#!/bin/bash
# script to send custom headers to servers
curl -s -H "X-MySchool-User-Id: 98" "$1"
