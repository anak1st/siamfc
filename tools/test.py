from __future__ import absolute_import

import os
import sys
abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(abs_path)


from got10k.experiments import *
from siamfc import TrackerSiamFC


if __name__ == '__main__':
    net_path = './model/_siamfc_alexnet_e50.pth'
    tracker = TrackerSiamFC(net_path=net_path)

    # e = ExperimentOTB(root_dir='D:/Downloads/Datasets/OTB100/data', version=2015)
    e = ExperimentGOT10k(root_dir='D:/Downloads/Datasets/GOT10k', subset='val')
    e.run(tracker, visualize=True)
    e.report([tracker.name])
