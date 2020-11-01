if [ ! -d ./skipthoughts/models ]
then
    mkdir skipthoughts/models
    wget -P ./skipthoughts/models http://www.cs.toronto.edu/~rkiros/models/dictionary.txt
    wget -P ./skipthoughts/models http://www.cs.toronto.edu/~rkiros/models/utable.npy
    wget -P ./skipthoughts/models http://www.cs.toronto.edu/~rkiros/models/btable.npy
    wget -P ./skipthoughts/models http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz
    wget -P ./skipthoughts/models http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz.pkl
    wget -P ./skipthoughts/models http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz
    wget -P ./skipthoughts/models http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz.pkl
fi
