#!/bin/bash

git pull
python make_md.py
git add *
git commit -m "Update"
git push
