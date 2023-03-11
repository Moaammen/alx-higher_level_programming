#!/usr/bin/python3
if __name__ == "__main__":
    """hidden_discovery"""
    import hidden_4

    magic = dir(hidden_4)
    for name in magic:
        if name[:2] != "__":
            print(name)