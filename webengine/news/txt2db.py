 
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webengine.settings')

import sys
sys.path.append('..')
from models import NewsInfo


def bulk_add():
    data_list = []
    with open('phpmyadmin.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            parts = line.split(',')
            course = NewsInfo(cour_id=parts[0], course=parts[1], grade=parts[2])
            data_list.append(course)
        NewsInfo.objects.bulk_create(data_list)
 
if __name__ == "__main__":

    bulk_add()

    print('Done!')
