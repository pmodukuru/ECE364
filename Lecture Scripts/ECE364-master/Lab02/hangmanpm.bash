#! /bin/bash

list=(banana hello turnip)

let i=$RANDOM%3
val=${list[i]}

val="Bannana"

set $val

echo $1