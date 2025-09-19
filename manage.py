#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
Este é um wrapper que aponta para src/manage.py
"""
import os
import sys
import subprocess

# Executar o manage.py real em src/
subprocess.call([sys.executable, 'src/manage.py'] + sys.argv[1:])