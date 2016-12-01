#!/bin/sh

if [ $# -ne 1 ]; then
    echo "./build.sh version"
    exit 1
fi

cp -r HAProxy.docset-tmpl HAProxy-$1.docset
sed -i "" -e "s/VERSION/$1/g" HAProxy-$1.docset/Contents/Info.plist
cp -r Documents/$1 HAProxy-$1.docset/Contents/Resources/Documents/
python gen.py $1
mv docSet.dsidx HAProxy-$1.docset/Contents/Resources/
