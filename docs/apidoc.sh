#!/bin/bash

sphinx-apidoc -M -f -o . .. "../**/migrations/*" "../manage.py" "../run_pylint.py"