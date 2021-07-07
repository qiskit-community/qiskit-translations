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

curl https://downloads.rclone.org/rclone-current-linux-amd64.deb -o rclone.deb
sudo apt-get install -y ./rclone.deb

RCLONE_CONFIG_PATH=$(rclone config file | tail -1)

set -e

# Clone the sources files and po files to ml_docs_source/
git clone --depth=1 $ML_SOURCE_REPOSITORY ml_docs_source
rclone sync -v --exclude='locale/**' ml_docs_source/docs machine-learning/docs

pushd $SOURCE_DIR/machine-learning/docs

# Make translated document
# FIXME: to install only from the stable branch
pip install -e ml_docs_source/.

sphinx-build -b html -D content_prefix=documentation/machine-learning -D language=$TRANSLATION_LANG . _build/html/locale/$TRANSLATION_LANG

rm -rf $SOURCE_DIR/$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/.doctrees/ \
    $SOURCE_DIR/$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/LC_MESSAGES/_sources/

echo "ls from current dir"
pwd
ls -R

echo "move html files from _build/ to build/"
mv $SOURCE_DIR/$SOURCE_DOC_DIR/* $SOURCE_DIR/build/

popd
