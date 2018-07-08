#!/bin/sh
cd ~
mkdir test
cd test

for (i=0; i<10; i++); do
    touch test_$i.txt
done

echo "hello world"

