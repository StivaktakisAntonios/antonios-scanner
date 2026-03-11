#!/usr/bin/env python3

import sys
import platform

def main():
    print(" Security Scanner")
    print("-" * 50)
    print(f"Version of python: {sys.version}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print("-" * 50)
    print("This container is scanned for vulnerabilitie")
    print("-" * 50)

if __name__ == "__main__":
    main()
