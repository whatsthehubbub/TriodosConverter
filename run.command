#!/bin/bash

cd "$(dirname "$0")"

echo $PWD

virtualenv ENV
source ENV/bin/activate

pip install xlrd
python convert.py