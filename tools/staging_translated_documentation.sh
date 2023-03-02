#!/bin/bash

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Script for publishing production the translated documentation.

# Non-travis variables used by this script.
SOURCE_REPOSITORY="https://github.com/Qiskit/qiskit.git"
SOURCE_DOC_DIR="_build/html"
SOURCE_DIR=`pwd`

curl https://downloads.rclone.org/rclone-current-linux-amd64.deb -o rclone.deb
sudo apt-get install -y ./rclone.deb

RCLONE_CONFIG_PATH=$(rclone config file | tail -1)

set -e

# Clone the sources files and po files to $SOURCE_DIR/docs_source
git clone --depth=1 $SOURCE_REPOSITORY docs_source

rclone sync -v --exclude='locale/**' docs_source/docs docs

pushd $SOURCE_DIR/docs

echo "after rclone"
ls -ll

cd ..
pwd
echo "before sphinx build"

# Make translated document
sphinx-build -b html -j auto -D content_prefix=documentation -D language=$TRANSLATION_LANG docs/ docs/_build/html/locale/$TRANSLATION_LANG

cd docs

rm -rf $SOURCE_DIR/$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/.doctrees/ \
rm -rf $SOURCE_DIR/$SOURCE_DOC_DIR/locale/$TRANSLATION_LANG/_sources/

echo "ls from current dir"
pwd
ls -R

echo "move html files from _build/ to build/"
mv $SOURCE_DIR/docs/$SOURCE_DOC_DIR/* $SOURCE_DIR/build/

popd
