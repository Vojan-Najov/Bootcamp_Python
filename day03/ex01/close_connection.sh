#!/bin/bash

redis-cli client list | grep cmd=subscribe | cut -d ' ' -f 1 | \
    cut -d '=' -f 2 | awk '{print "CLIENT KILL ID " $0}' | redis-cli -x
