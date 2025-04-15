#!/bin/bash

du -sh ./*/ | sort | head -n 5 > test.txt
