#!/bin/bash

set -e 

FILES_WITH_MAIN=`grep -l main *.py | grep -v streamlit_app`
for F in $FILES_WITH_MAIN; do
    echo "Running $F"
    python $F
    echo "DONE: $F"
    echo
done

echo "Finished."

