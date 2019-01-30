#!/usr/bin/python

import json

def main():
    print(json.dumps(dict(changed=False, source='new content-adjacent')))


if __name__ == '__main__':
    main()


