#!/usr/bin/pyhton3
"""0-main"""
from models.base import Base

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)
    b2 = Base()
    print(b2.id)
    b3 = Base(12)
    print(b3.id)
