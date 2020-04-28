#!/bin/bash
kill $(ps aux | grep "chrome")
python3 /Users/patiencempofu/PycharmProjects/browser_manager/src/browser.py /Users/patiencempofu/PycharmProjects/browser_manager/src/websites.txt chrome
exit 0