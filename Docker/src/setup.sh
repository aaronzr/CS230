#!/bin/bash
bash MeanSum/scripts/install_python_pkgs.sh
python MeanSum/scripts/update_tensorboard.py
bash MeanSum/scripts/preprocess_data.sh
# test
