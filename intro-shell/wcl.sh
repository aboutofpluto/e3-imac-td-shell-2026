#!/bin/bash

count=0

function count_words() {
 printf "%d words in line %d\n" $(echo $1 | wc -w) $2
}

while IFS='' read -r line || [[ -n "${line}" ]]; do
 ((count++))
 count_words "$line" $count
done < "$1"
