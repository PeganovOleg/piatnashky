#!/usr/bin/env python3
import sys
import os

# Добавляем текущую директорию в путь
sys.path.insert(0, os.getcwd())

from hearts_puzzle import main

if __name__ == "__main__":
    main()