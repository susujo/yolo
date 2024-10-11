from ultralytics.data.split_dota import split_trainval,split_test

#split train and val set,with labels
split_trainval(
    data_root='F:/研究生/DOTAv',
    save_dir='F:/研究生/DOTAv/1',
    rates=[1.0],
    gap=500
)

#split test set,without labels
#split_test(
    #data_root='F:/研究生/DOTAv',
    #save_dir='F:/研究生/DOTAv',
    #rates=[1.0],
    #gap=500
#)