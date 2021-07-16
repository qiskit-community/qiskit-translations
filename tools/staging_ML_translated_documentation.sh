#!/bin/bash

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Script for publishing translated ML documentation to staging site.

# Non-travis variables used by this script.
ML_SOURCE_REPOSITORY="https://github.com/Qiskit/qiskit-machine-learning.git"
SOURCE_DOC_DIR="docs/_build/html"
SOURCE_DIR=`pwd`
STABLE_VERSION=`cat ./qiskit_machine_learning/VERSION.txt`
FORMATED_VERSION=`echo $STABLE_VERSION | cut -d "." -f -2`

set -e

# Clone the sources files and po files to ml_docs_source/
git clone $ML_SOURCE_REPOSITORY ml_docs_source
cd ml_docs_source/
git fetch
git checkout stable/$FORMATED_VERSION

cd docs/
mkdir -p locale/  && cp -r ../../docs/locale/* locale/

# Make translated document
sphinx-build -b html -D content_prefix=documentation/machine-learning -D language=$TRANSLATION_LANG . _build/html/locale/$TRANSLATION_LANG

rm -rf $SOURCE_DIR/$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/.doctrees/ \
    $SOURCE_DIR/$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/LC_MESSAGES/_sources/

echo "make build dir "
mkdir -p $SOURCE_DIR/build/

echo "move html files from _build/ to build/"
mv $SOURCE_DIR/ml_docs_source/$SOURCE_DOC_DIR/locale/* $SOURCE_DIR/build/
