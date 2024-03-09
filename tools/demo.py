from __future__ import absolute_import

import os
import sys
abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(abs_path)


import glob
import numpy as np


from siamfc import TrackerSiamFC


if __name__ == '__main__':
    root_dir = 'D:/Downloads/Datasets/OTB100/data'
    seq_dir = os.path.join(root_dir, 'Crossing/')
    img_files = sorted(glob.glob(seq_dir + 'img/*.jpg'))
    anno = np.loadtxt(seq_dir + 'groundtruth_rect.txt')
    
    net_path = './model/siamfc_alexnet_e50.pth'
    tracker = TrackerSiamFC(net_path=net_path)
    tracker.track(img_files, anno[0], visualize=True)
