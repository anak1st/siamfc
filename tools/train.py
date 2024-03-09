from __future__ import absolute_import

import os
import sys
abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(abs_path)


from got10k.datasets import *

from siamfc import TrackerSiamFC


if __name__ == '__main__':
    seqs = GOT10k('D:/Downloads/Datasets/GOT10k', subset='train', return_meta=True)

    tracker = TrackerSiamFC()
    tracker.train_over(seqs)
