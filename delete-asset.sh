#!/bin/sh

set -eu

curl \
    -o /dev/null -s -w "%{http_code}\n" \
    -H "Authorization: token $1" \
    -X DELETE \
    "https://api.github.com/repos/ProdriveTechnologies/texlive-modular/releases/assets/$2"
