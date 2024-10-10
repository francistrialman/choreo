#!/usr/bin/env python
# coding=utf-8
import datetime

date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open('README.md', 'w')as f:
    f.write(date)