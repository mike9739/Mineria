import numpy as np
def read_file(file):
    content = []
    with open(file,encoding='utf-8') as reader:
        for line  in reader:
            content.append(line.rstrip())
    return content

def sub_sample(data,*idxs):
    sample = []
    for idx in idxs:
        sample.extend([data[i] for i in idx])
    return sample

def write_file(file,data):
    with open(file,'w',encoding='utf-8') as writer:
        for line in data:
            writer.write(line+'\n')
main_dir = 'C:/Users/migu_/OneDrive - Universidad de Guanajuato/Mineria de datos'
data_file = main_dir+'fb_post_all.txt'
labels_file = main_dir+'labels.txt'

data = read_file(data_file)
labels = read_file(labels_file)

idx_1=np.random.permutation(70)
idx_2=np.random.permutation(list(range(70,140)))
idx_3=np.random.permutation(list(range(140,210)))

train = sub_sample(data,idx_1[:42],idx_2[:42],idx_3[:42])



