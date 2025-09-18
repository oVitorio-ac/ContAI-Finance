#!/usr/bin/env python
"""
Script para executar todos os testes do projeto ContAI Finance
"""
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'contai_finance.settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    
    print("🧪 Executando todos os testes do ContAI Finance...")
    print("=" * 50)
    
    # Executar todos os testes
    failures = test_runner.run_tests(["tests"])
    
    if failures:
        print(f"\n❌ {failures} teste(s) falharam!")
        sys.exit(1)
    else:
        print("\n✅ Todos os testes passaram!")
        sys.exit(0)