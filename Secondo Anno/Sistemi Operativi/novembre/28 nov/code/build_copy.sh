#!/bin/sh

gcc copy_file_with_seek.c -o copy_seek
./copy_seek file1.txt file2.txt $1
