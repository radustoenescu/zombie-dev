#!/bin/bash

FILE=$1
HEAD_TAG_LINE=$(cat $FILE | grep head -m 1 -n | cut -d: -f1)

cat $FILE | head -n $HEAD_TAG_LINE > out
cat >> out <<CODE
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-33188271-5"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'UA-33188271-5');
    </script>
CODE
cat $FILE | tail -n +$(( $HEAD_TAG_LINE  + 1 )) >> out

mv out $FILE
