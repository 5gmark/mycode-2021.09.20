#!/usr/bin/env python3

def mark():
    print("\nThis is mark() in main1.py")
    print("__name__ = " + __name__)

def main():
    print("This is main1.py.")
    print("__name__ = " + __name__)
    mark()

if __name__ == "__main__":
    main()
