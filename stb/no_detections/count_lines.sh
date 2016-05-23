#!/bin/zsh
source ~/.aliases.sh
for file in *.json
do
 # do something on "$file"
 echo $file
 pprjson "$file" | wc -l 
 done

