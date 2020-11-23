#!/bin/bash
sleep 3
PID=$(pgrep RDR2.exe); kill -s SIGSTOP $PID; kill -s SIGCONT $PID
sleep 3

