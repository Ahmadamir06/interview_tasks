#!/bin/bash
if [ -f "$1" ]; then
	INF=$( grep "INFO" "$1" |wc -l)
	WAR=$( grep "WARNING" "$1" | wc -l)
	ERR=$( grep "ERROR" "$1" | wc -l )
	echo "inf: $INF, warnings: $WAR, errors: $ERR"
	grep "ERROR" "$1" > "errors_only.log"
else
	echo "Error, no such file as $1"
fi
