import os
import glob
import shutil

names = glob.glob("/mnt/moonfs/audio-m2/dcyang/exp_data/rec_demo/music/ours/*.wav")

keys = []
for name in names:
    bs_name = os.path.basename(name)
    keys.append(bs_name)

source_path = '/mnt/moonfs/audio-m2/dcyang/exp_data/music_data'

names = glob.glob(f"{source_path}/*.wav")
for name in names:
    bs_name = os.path.basename(name)
    if bs_name in keys:
        shutil.copyfile(name, '/mnt/moonfs/audio-m2/dcyang/exp_data/rec_demo/music/gt/'+bs_name)
    

