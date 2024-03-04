#!/bin/bash

set -e 

FILES_WITH_MAIN=`grep -l main *.py`
for F in $FILES_WITH_MAIN; do
    echo "Running $F"
    python $F
    echo
done
