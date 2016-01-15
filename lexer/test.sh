#!/bin/sh
echo "running test"
../bin/pygmentize -O full -f html -o /tmp/example.html examplefiles/example.osexample

echo "please open /tmp/example.html in your fav. browser"
