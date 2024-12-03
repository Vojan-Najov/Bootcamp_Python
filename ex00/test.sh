#! /bin/bash

python=`which python3`

data='00000254b208c0f43409d8dc00439896
000000434dd5469464f5cafd8ffe3609
00000f31eaabadef948f28d1
e7a1ee0b7de74786a2c0180bcdb632da
0000085a34260d1c84e89865c210ceb4
073f7873a75c457cbb3307d729501cb5
b7c93ff4cc1c4e0486a8fc66605
fe564b26f25e47c393d07e494021479e
a5dff06057d14566b45caef813511738
0000071f49cffeaea4184be3d507086v'

cat >data_hashes_10lines.txt <<<$data

test='test1'
res=$(echo `cat data_hashes_10lines.txt | $python blocks.py 10`)
ans='00000254b208c0f43409d8dc00439896 0000085a34260d1c84e89865c210ceb4 0000071f49cffeaea4184be3d507086v'
if [ "$res" != "$ans" ]; then echo "Failed $test"; else echo "Successed $test"; fi

test='test2'
res=$(echo `cat data_hashes_10lines.txt | $python blocks.py 1`)
ans='00000254b208c0f43409d8dc00439896'
if [ "$res" != "$ans" ]; then echo "Failed $test"; else echo "Successed $test"; fi

test='test3'
res=$(echo `cat data_hashes_10lines.txt | $python blocks.py 0`)
ans=''
if [ "$res" != "$ans" ]; then echo "Failed $test"; else echo "Successed $test"; fi

test='test4'
res=$(echo `cat data_hashes_10lines.txt | $python blocks.py 8`)
ans='00000254b208c0f43409d8dc00439896 0000085a34260d1c84e89865c210ceb4'
if [ "$res" != "$ans" ]; then echo "Failed $test"; else echo "Successed $test"; fi

test='test5'
res=$(echo `cat data_hashes_10lines.txt | $python blocks.py 100`)
ans='00000254b208c0f43409d8dc00439896 0000085a34260d1c84e89865c210ceb4 0000071f49cffeaea4184be3d507086v'
if [ "$res" != "$ans" ]; then echo "Failed $test"; else echo "Successed $test"; fi

test='test6'
res=$(echo `cat data_hashes_10lines.txt | $python blocks.py -1`)
ans='incorrect arguments'
if [ "$res" != "$ans" ]; then echo "Failed $test"; else echo "Successed $test"; fi

test='test7'
res=$(echo `cat data_hashes_10lines.txt | $python blocks.py asdads`)
ans='incorrect arguments'
if [ "$res" != "$ans" ]; then echo "Failed $test"; else echo "Successed $test"; fi

test='test8'
res=$(echo `cat data_hashes_10lines.txt | $python blocks.py 10 21`)
ans='incorrect arguments'
if [ "$res" != "$ans" ]; then echo "Failed $test"; else echo "Successed $test"; fi

rm data_hashes_10lines.txt
