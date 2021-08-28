for d in */ ; do
    echo "$d"
    cd $d
    sls deploy
    cd ..
    
done