import sys
import os


def count_files(root_dir: str) -> list:
    dir_nums = []
    for dir in os.listdir(root_dir):
        if dir == 'list.txt':
            continue
        dir_num = int(dir.split('_')[-1])
        dir_nums.append(dir_num)

    dir_nums.sort()
    print('=' * 40)
    print(f"len: {len(dir_nums)}, min: {min(dir_nums)}, max: {max(dir_nums)}")

    return dir_nums


def print_all_dirs(root_dir: str) -> dict:
    extensions_all = {}
    for root, dirs, files in os.walk(root_dir):
        # print(root, len(files))

        extensions = {}
        for file in files:
            ext = file.split('.')[-1]
            if ext not in extensions:
                extensions[ext] = 0
            extensions[ext] += 1

            if ext not in extensions_all:
                extensions_all[ext] = 0
            extensions_all[ext] += 1

    print('=' * 40)
    print(extensions_all)
    print(f"avg jpg files per dir: {extensions_all['jpg'] / len(dir_nums):.2f}")

    return extensions_all


if __name__ == "__main__":
    root_dir = 'D:/Downloads/Datasets/GOT10k/train'

    dir_nums = count_files(root_dir)
    extensions_all = print_all_dirs(root_dir)

    
