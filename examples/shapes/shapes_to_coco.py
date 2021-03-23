#!/usr/bin/env python3

import sys
import datetime
import json
import os
import re
import fnmatch
from PIL import Image
import numpy as np
import sys
sys.path.append('/content/pycococreator')

from pycococreatortools import pycococreatortools




outputname = sys.argv[1]
json_name = sys.argv[2]

ROOT_DIR = outputname
IMAGE_DIR = os.path.join(ROOT_DIR, 'JPEGImages')
ANNOTATION_DIR = os.path.join(ROOT_DIR,"LabelImages")



INFO = {
    "description": "AndySer Brandname Dataset",
    "url": "https://github.com/waspinator/pycococreator",
    "version": "0.1.0",
    "year": 2021,
    "contributor": "Waspinator,AndyLee",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}

LICENSES = [
    {
        "id": 1,
        "name": "Attribution-NonCovivaercial-ShareAlike License",
        "url": "http://creativecovivaons.org/licenses/by-nc-sa/2.0/"
    }
]

CATEGORIES = [
    {
        'id': 1,
        'name': '3m',
        'supercategory': 'brandname',
    },
    {
        'id': 2,
        'name': 'andes',
        'supercategory': 'brandname',
    },
    {
        'id': 3,
        'name': 'cocacola',
        'supercategory': 'brandname',
    },
    {
        'id': 4,
        'name': 'crayola',
        'supercategory': 'brandname',
    },
    {
        'id': 5,
        'name': 'folgers',
        'supercategory': 'brandname',
    },
    {
        'id': 6,
        'name': 'heineken',
        'supercategory': 'brandname',
    },
    {
        'id': 7,
        'name': 'hunts',
        'supercategory': 'brandname',
    },
    {
        'id': 8,
        'name': 'kellogg',
        'supercategory': 'brandname',
    },
    {
        'id': 9,
        'name': 'kleenex',
        'supercategory': 'brandname',
    },
    {
        'id': 10,
        'name': 'kotex',
        'supercategory': 'brandname',
    },
    {
        'id': 11,
        'name': 'libava',
        'supercategory': 'brandname',
    },
    {
        'id': 12,
        'name': 'macadamia',
        'supercategory': 'brandname',
    },
    {
        'id': 13,
        'name': 'milo',
        'supercategory': 'brandname',
    },
    {
        'id': 14,
        'name': 'mm',
        'supercategory': 'brandname',
    },
    {
        'id': 15,
        'name': 'pocky',
        'supercategory': 'brandname',
    },
    {
        'id': 16,
        'name': 'raisins',
        'supercategory': 'brandname',
    },
    {
        'id': 17,
        'name': 'stax',
        'supercategory': 'brandname',
    },
    {
        'id': 18,
        'name': 'swissmiss',
        'supercategory': 'brandname',
    },
    {
        'id': 19,
        'name': 'vanish',
        'supercategory': 'brandname',
    },
    {
        'id': 20,
        'name': 'viva',
        'supercategory': 'brandname',
    },
    
]

def filter_for_jpeg(root, files):
    file_types = ['*.jpeg', '*.jpg']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    
    return files

def filter_for_annotations(root, files, image_filename):
    file_types = ['*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    basename_no_extension = os.path.splitext(os.path.basename(image_filename))[0]
    file_name_prefix = basename_no_extension + '.*'
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    files = [f for f in files if re.match(file_name_prefix, os.path.splitext(os.path.basename(f))[0])]

    return files

def main():

    coco_output = {
        "info": INFO,
        "licenses": LICENSES,
        "categories": CATEGORIES,
        "images": [],
        "annotations": []
    }

    image_id = 1
    segmentation_id = 1
    
    # filter for jpeg images
    for root, _, files in os.walk(IMAGE_DIR):
        image_files = filter_for_jpeg(root, files)

        # go through each image
        for image_filename in image_files:
            
            image = Image.open(image_filename)
            image_info = pycococreatortools.create_image_info(
                image_id, os.path.basename(image_filename), image.size)
            coco_output["images"].append(image_info)

            # filter for associated png annotations
            for root, _, files in os.walk(ANNOTATION_DIR):
                annotation_files = filter_for_annotations(root, files, image_filename)

                # go through each associated annotation
                for annotation_filename in annotation_files:
                    
                    if '3m' in annotation_filename:
                        class_id  = 1
                    elif 'andes' in annotation_filename:
                        class_id = 2
                    elif 'cocacola' in annotation_filename:
                        class_id = 3
                    elif 'crayola' in annotation_filename:
                        class_id = 4
                    elif 'folgers' in annotation_filename:
                        class_id = 5
                    elif 'heineken' in annotation_filename:
                        class_id = 6
                    elif 'hunts' in annotation_filename:
                        class_id = 7
                    elif 'kellogg' in annotation_filename:
                        class_id = 8
                    elif 'kleenex' in annotation_filename:
                        class_id = 9
                    elif 'kotex' in annotation_filename:
                        class_id = 10
                    elif 'libava' in annotation_filename:
                        class_id = 11
                    elif 'macadamia' in annotation_filename:
                        class_id = 12
                    elif 'milo' in annotation_filename:
                        class_id = 13
                    elif 'mm' in annotation_filename:
                        class_id = 14
                    elif 'pocky' in annotation_filename:
                        class_id = 15
                    elif 'raisins' in annotation_filename:
                        class_id = 16
                    elif 'stax' in annotation_filename:
                        class_id = 17
                    elif 'swissmiss' in annotation_filename:
                        class_id = 18
                    elif 'vanish' in annotation_filename:
                        class_id = 19
                    else:
                        class_id = 20
                    
                    category_info = {'id': class_id, 'is_crowd': 'crowd' in image_filename}
                    binary_mask = np.asarray(Image.open(annotation_filename)
                        .convert('1')).astype(np.uint8)
                    annotation_info = pycococreatortools.create_annotation_info(
                        segmentation_id, image_id, category_info, binary_mask,
                        image.size, tolerance=2)
                    print(str(image_id)+ " images write into the json file,{} left".format(len(image_files)-image_id))
                    if annotation_info is not None:
                        coco_output["annotations"].append(annotation_info)

                    segmentation_id = segmentation_id + 1

            image_id = image_id + 1

    with open('{}/{}.json'.format(ROOT_DIR,json_name), 'w') as output_json_file:
        json.dump(coco_output, output_json_file)


if __name__ == "__main__":
    main()
