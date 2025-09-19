#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
Este é um wrapper que aponta para src/manage.py
"""
import os
import sys

# Executar o manage.py real em src/
os.chdir('src')
exec(open('manage.py').read())