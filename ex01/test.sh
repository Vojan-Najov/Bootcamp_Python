#!/bin/bash

python=`which python3`


test=1
arg="The only way everyone reaches Brenda rapidly is delivering groceries explicitly"
res=`$python decypher.py "$arg"`
ans='Towerbridge'

if [ "$res" != "$ans" ]; then
    echo "Test$test failed";
else
    echo "Test$test successed";
fi

test=2
arg="Britain is Great because everyone necessitates"
res=`$python decypher.py "$arg"`
ans='Bigben'

if [ "$res" != "$ans" ]; then
    echo "Test$test failed";
else
    echo "Test$test successed";
fi

test=3
arg="Have you delivered eggplant pizza at restored keep?"
res=`$python decypher.py "$arg"`
ans='Hydepark'

if [ "$res" != "$ans" ]; then
    echo "Test$test failed";
else
    echo "Test$test successed";
fi

test=4
res=`$python decypher.py 'a' 'b'`
ans='incorrect arguments'

if [ "$res" != "$ans" ]; then
    echo "Test$test failed";
else
    echo "Test$test successed";
fi

test=5
res=`$python decypher.py`
ans='incorrect arguments'
if [ "$res" != "$ans" ]; then
    echo "Test$test failed";
else
    echo "Test$test successed";
fi

