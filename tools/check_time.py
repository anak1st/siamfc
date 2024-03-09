import os
import sys
import time


def read_files(root_dir: str) -> list:
    res = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".txt"):
                res.append(os.path.join(root, file))
    return res


def read_file(file: str) -> list:
    res = []
    with open(file, 'r') as f:
        for line in f:
            res.append(float(line.strip()))

    return res


if __name__ == "__main__":
    root_dir = 'D:/GitHub/siamfc/results/OTB2015/SiamFC/times'

    files = read_files(root_dir)

    times = {}
    for f in files:
        file_name = os.path.basename(f)
        file_name = file_name.split('_')[0]
        times[file_name] = read_file(f)

    fps = {}
    for k, v in times.items():
        fps[k] = len(v) / sum(v)

    for k, v in fps.items():
        print(f"{k.ljust(15)} fps: {v:.2f}")

    print('=' * 40)
    print(f"total files: {len(files)}")
    print(f"max fps: {max(fps, key=fps.get)}: {max(fps.values()):.2f}")
    print(f"min fps: {min(fps, key=fps.get)}: {min(fps.values()):.2f}")
    print(f"avg fps: {sum(fps.values()) / len(fps):.2f}")
