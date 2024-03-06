from __future__ import absolute_import

import os
import sys
abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(abs_path)
print(abs_path)


from got10k.experiments import *
from siamfc import TrackerSiamFC


if __name__ == '__main__':
    net_path = 'D:/Repos/siamfc-pytorch/model/siamfc_alexnet_e50.pth'
    tracker = TrackerSiamFC(net_path=net_path)

    root_dir = 'D:/Downloads/Datasets/OTB100/data'
    e = ExperimentOTB(root_dir, version=2015)
    e.run(tracker, visualize=True)
    e.report([tracker.name])
