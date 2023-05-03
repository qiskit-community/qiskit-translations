#!/bin/bash

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Script for publishing translated runtime documentation to staging site.

# Non-travis variables used by this script.

RUNTIME_SOURCE_REPOSITORY="https://github.com/Qiskit/qiskit-ibm-runtime.git"
SOURCE_DOC_DIR="_build/html"
SOURCE_DIR=`pwd`

STABLE_VERSION=`cat ./qiskit_ibm_runtime/VERSION.txt`
FORMATED_VERSION=`echo $STABLE_VERSION | cut -d "." -f -2`

curl https://downloads.rclone.org/rclone-current-linux-amd64.deb -o rclone.deb
sudo apt-get install -y ./rclone.deb

RCLONE_CONFIG_PATH=$(rclone config file | tail -1)

set -e

# Clone the sources files and po files to runtime_docs_source/
git clone $RUNTIME_SOURCE_REPOSITORY runtime_docs_source
cd runtime_docs_source/
git fetch
git checkout stable/$FORMATED_VERSION

cd docs
mkdir -p locale/  && cp -r ../../docs/locale/* locale/

# Make translated document
sphinx-build -b html -D content_prefix=documentation/partners/qiskit_ibm_runtime -D language=$TRANSLATION_LANG . _build/html/locale/$TRANSLATION_LANG

echo "current directory"
pwd

rm -rf ./$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/.doctrees/
rm -rf ./$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/_sources/

echo "ls"
ls -a ./$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/

echo "move html files from _build/ to build/"
mv -v $SOURCE_DIR/runtime_docs_source/docs/$SOURCE_DOC_DIR/* $SOURCE_DIR/build/
