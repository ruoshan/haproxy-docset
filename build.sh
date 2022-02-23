#!/bin/sh

if [ $# -ne 1 ]; then
    echo "./build.sh version (eg.2.4.0)"
    exit 1
fi

rm -rf HAProxy.docset HAProxy.tgz

cp -r HAProxy.docset-tmpl HAProxy.docset
sed -i "" -e "s/VERSION/$1/g" HAProxy.docset/Contents/Info.plist
cp -r Documents/$1 HAProxy.docset/Contents/Resources/Documents/
./gen.py $1
mv docSet.dsidx HAProxy.docset/Contents/Resources/

tar zcf HAProxy.tgz HAProxy.docset
