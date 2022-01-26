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

# Script for publishing translated finance documentation to staging site.

# Non-travis variables used by this script.
FINANCE_SOURCE_REPOSITORY="https://github.com/Qiskit/qiskit-finance.git"
SOURCE_DOC_DIR="docs/_build/html"
SOURCE_DIR=`pwd`
STABLE_VERSION=`cat ./qiskit_finance/VERSION.txt`
FORMATED_VERSION=`echo $STABLE_VERSION | cut -d "." -f -2`

set -e

# Clone the sources files and po files to finance_docs_source/
git clone $FINANCE_SOURCE_REPOSITORY finance_docs_source
cd finance_docs_source/
git checkout stable/$FORMATED_VERSION

cd docs/
mkdir -p locale/  && cp -r ../../docs/locale/* locale/

# Make translated document
sphinx-build -b html -D content_prefix=documentation/finance -D language=$TRANSLATION_LANG . _build/html/locale/$TRANSLATION_LANG

rm -rf $SOURCE_DIR/$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/.doctrees/ \
rm -rf $SOURCE_DIR/$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/LC_MESSAGES/_sources/

echo "make finance dir "
mkdir -p $SOURCE_DIR/finance/

echo "move html files from _build/ to finance/"
mv $SOURCE_DIR/finance_docs_source/$SOURCE_DOC_DIR/locale/* $SOURCE_DIR/finance/
