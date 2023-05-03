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

openssl aes-256-cbc -K $encrypted_rclone_key -iv $encrypted_rclone_iv -in ../tools/rclone.conf.enc -out $RCLONE_CONFIG_PATH -d

echo "Pushing built Runtime translated docs to qiskit.org/ecosystem"
rclone sync --progress ./_build/html/locale/$TRANSLATION_LANG IBMCOS:qiskit-org-web-resources/ecosystem/ibm-runtime/locale/$TRANSLATION_LANG

# Push to qiskit.org/documentation
rclone sync --progress ./_build/html/locale/$TRANSLATION_LANG IBMCOS:qiskit-org-web-resources/documentation/partners/qiskit_ibm_runtime/locale/$TRANSLATION_LANG
