#!/bin/bash

python=`which python3`

data='*d&t*
**h**
*l*!*'
cat >m.txt <<<$data
test=1
res=`$python mfinder.py <m.txt`
ans='True'
if [ "$res" == "$ans" ]; then
    echo "Tets$test successed";
else
    echo "Tets$test failed";
fi
    
data='*****
*****
*****'
cat >m.txt <<<$data
test=2
res=`$python mfinder.py <m.txt`
ans='False'
if [ "$res" == "$ans" ]; then
    echo "Tets$test successed";
else
    echo "Tets$test failed";
fi
 
data='*s*f*
**f**
*a***'
cat >m.txt <<<$data
test=3
res=`$python mfinder.py <m.txt`
ans='False'
if [ "$res" == "$ans" ]; then
    echo "Tets$test successed";
else
    echo "Tets$test failed";
fi


data='*s*f*6
**f**
*a***'
cat >m.txt <<<$data
test=4
res=`$python mfinder.py <m.txt`
ans='Error'
if [ "$res" == "$ans" ]; then
    echo "Tets$test successed";
else
    echo "Tets$test failed";
fi


data='*s*f
**f**
*a***'
cat >m.txt <<<$data
test=5
res=`$python mfinder.py <m.txt`
ans='Error'
if [ "$res" == "$ans" ]; then
    echo "Tets$test successed";
else
    echo "Tets$test failed";
fi


data='*d&t*
**h**
*l*!*
*****'
cat >m.txt <<<$data
test=6
res=`$python mfinder.py <m.txt`
ans='Error'
if [ "$res" == "$ans" ]; then
    echo "Tets$test successed";
else
    echo "Tets$test failed";
fi

data='*d&t*
**h**'
cat >m.txt <<<$data
test=7
res=`$python mfinder.py <m.txt`
ans='Error'
if [ "$res" == "$ans" ]; then
    echo "Tets$test successed";
else
    echo "Tets$test failed";
fi

rm m.txt
