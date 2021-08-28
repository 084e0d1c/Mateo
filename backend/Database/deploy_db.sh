for d in */ ; do
    echo "$d"
    cd $d
    sls deploy --stage dev
    cd ..
    
done