import os, sys
from PIL import Image
import math
import argparse
from WaterSort import WaterSort

# PIXEL WIDTH AND HEIGHT for iPhone 12 Pro Resolution RATIO
NUM_BOTTLES_MAP_PERCETAGE = {
    11: [
        90/946, 240/946, 400/946, 550/946, 700/946, 850/946,
        120/946, 300/946, 470/946, # Emtpy, Empty
    ],
    14: [
        75/946, 200/946, 340/946, 475/946, 600/946, 740/946, 875/946,
        75/946, 200/946, 340/946, 475/946, 600/946, # Emtpy, Empty
    ],
}

ROW_1_HEIGHT_B4 = 735/2048
ROW_1_HEIGHT_B3 = 815/2048
ROW_1_HEIGHT_B2 = 895/2048
ROW_1_HEIGHT_B1 = 975/2048

ROW_2_HEIGHT_B4 = 1310/2048
ROW_2_HEIGHT_B3 = 1390/2048
ROW_2_HEIGHT_B2 = 1470/2048
ROW_2_HEIGHT_B1 = 1550/2048

PIXEL_MAP_INT = {}



def get_coordinates(image_path, num_bottles):
    img = Image.open(image_path) 
    img_width = img.width 
    img_height = img.height 

    bottles = {}
    top_row = math.ceil(num_bottles/2)
    bottom_row = math.floor(num_bottles/2)

    for i in range(top_row):
        width = NUM_BOTTLES_MAP_PERCETAGE[num_bottles][i]
        bottles[(i+1)] = [
            (width*img_width, ROW_1_HEIGHT_B1*img_height),
            (width*img_width, ROW_1_HEIGHT_B2*img_height),
            (width*img_width, ROW_1_HEIGHT_B3*img_height),
            (width*img_width, ROW_1_HEIGHT_B4*img_height)
        ]
    for i in range(top_row, bottom_row+top_row-2):
        width = NUM_BOTTLES_MAP_PERCETAGE[num_bottles][i]
        bottles[(i+1)] = [
            (width*img_width, ROW_2_HEIGHT_B1*img_height),
            (width*img_width, ROW_2_HEIGHT_B2*img_height),
            (width*img_width, ROW_2_HEIGHT_B3*img_height),
            (width*img_width, ROW_2_HEIGHT_B4*img_height)
        ]

    print(num_bottles, top_row, bottom_row)
    # print(bottles)
    return bottles

def get_pixel_values(image_path, coordinates):
    # Open the image
    image = Image.open(image_path)

    pixel_values = []

    # Iterate through each coordinate and retrieve pixel value
    for coordinate in coordinates:
        x, y = coordinate
        pixel_value = image.getpixel((x, y))
        pixel_value = tuple([ round(i) for i in pixel_value])
        pixel_values.append(pixel_value)

    return pixel_values


def get_bottle_integers(image_path, bottle_coords):
    integers = []
    pixel_values = get_pixel_values(image_path, bottle_coords)
    for i, coordinate in enumerate(bottle_coords):
        if pixel_values[i] not in PIXEL_MAP_INT:
            PIXEL_MAP_INT[pixel_values[i]] = len(PIXEL_MAP_INT)
        integers.append(PIXEL_MAP_INT[pixel_values[i]])
        print(f"{coordinate}: Value: {pixel_values[i]} {PIXEL_MAP_INT[pixel_values[i]]}")
    return integers


if __name__ == "__main__":
    # python3 ./ImageToGame.py IMAGE_PATH NUM_BOTTLES

    parser = argparse.ArgumentParser(description ='ImageToGame - Convert Phone Screenshot Into Solvable Game.')
    parser.add_argument('image_path', type=str, help ='Path to Screenshot', default=None)
    parser.add_argument('nb', type=int, help ='Number of Bottles', default=11)
    args = parser.parse_args()

    # image_path = '/home/happy/Pictures/watersort_level159.jpeg'
    # num_bottles = 14

    if args.image_path and args.nb:
        image_path = args.image_path
        num_bottles = args.nb

        all_bottle_coords = get_coordinates(image_path, num_bottles)

        bottles = [
            get_bottle_integers(image_path, bottle_coords=bottle_coords)
            for key, bottle_coords in all_bottle_coords.items()
        ] + [[],[]]

        print()
        for bottle in bottles:
            print(f"\t{bottle},")
        print()

        water_sort = WaterSort(bottles=bottles)
        water_sort._print_water_sort()

