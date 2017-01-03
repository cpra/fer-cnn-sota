
'''
Apply histogram equalization to every image in a directory
and save it to another directory with the same name.
~ Christopher
'''

# includes

import cv2

import os
import argparse

# parse args

parser = argparse.ArgumentParser(description='Apply histogram equalization to an image directory')
parser.add_argument('images', type=str, help='Path to a folder containing images')
parser.add_argument('dest', type=str, help='Path to a folder to which to write the results')
args = parser.parse_args()

assert(os.path.isdir(args.images))
assert(not os.path.exists(args.dest))

# convert

os.mkdir(args.dest)

n = 0
for fname in os.listdir(args.images):
    fpath = os.path.join(args.images, fname)
    if not os.path.isfile(fpath):
        continue

    print('{} ...'.format(fname))

    im = cv2.imread(fpath, cv2.IMREAD_UNCHANGED)
    assert(im.size > 0)

    im = cv2.equalizeHist(im)
    cv2.imwrite(os.path.join(args.dest, fname), im)

    n += 1

print('Processed {} images'.format(n))
