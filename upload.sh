#!/bin/sh

set -eu

for file in output/*; do
  echo "${file}"
  curl \
      -s -o /dev/null \
      -H "Content-Type: application/octet-stream" \
      -H "Authorization: token $1" \
      --data-binary "@${file}" \
      "https://uploads.github.com/repos/ProdriveTechnologies/texlive-modular/releases/$2/assets?name=$(basename "${file}")"
done
