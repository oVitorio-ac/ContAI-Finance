#!/usr/bin/env python
"""
Script para executar os testes do projeto ContAI Finance.
"""
import os
import sys
import subprocess

def main():
    """Executa os testes usando pytest."""
    # Adicionar src/ ao path (como faz o manage.py)
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

    # Definir settings do Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contai_finance.settings")

    # Executar pytest
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",
        "--tb=short",
        "--strict-markers"
    ]

    try:
        result = subprocess.run(cmd, cwd=os.path.join(os.path.dirname(__file__), 'src'))
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\nTestes interrompidos pelo usuário.")
        sys.exit(1)

if __name__ == "__main__":
    main()