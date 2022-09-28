#!/usr/bin/python3.8

if __name__ == "__main__":
    import hidden_4.pyc as hidden
    for value in dir(hidden):
        if value[0] != "_":
            print(value)
