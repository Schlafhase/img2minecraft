import cv2
import numpy as np
from PIL import Image
import glob
from scipy import spatial
from random import randint
import os
from src import findindices

def read_image(source: str) -> np.ndarray:

    with Image.open(source).convert("RGB") as im:
        im_arr = np.asarray(im)
        #im_arr = im_arr[..., ::-1]
    return im_arr

def create_img_array(images_filepath, img_size, logs=False, blacklist = []):
    if logs: print("Loading images")
    images = []
    filenames = []
    for file in os.listdir(images_filepath):
        if file in blacklist: continue
        if logs: print(f"Adding {file}")
        if file.endswith(".png"):
            images.append(cv2.resize(read_image(f"{images_filepath}/{file}"), (img_size, img_size)))
            filenames.append(file)

    if logs: print(f"Found {len(images)} images")
    if logs: print(images[0].shape)
    images_array = np.asarray(images)
    return (images_array, images, filenames)


def create_fill_commands(width, heigth):
    # max_fill = 32768
    # if not width*heigth > max_fill:
    #     return [f"fill ~ ~-1 ~ ~{width} ~-1 ~{heigth} bedrock"]
    # else:
    #     cmds = []
    #     heigth_chunks = heigth//25
    #     width_chunks = width//25
    #     for i in range(heigth_chunks):
    #         for j in range(width_chunks):
    #             cmds.append(f"fill ~{j*25} ~-1 ~{i*25} ~{(j+1)*25} ~-1 ~{(i+1)*25} bedrock")
    #     return cmds
    cmds = []
    for i in range(width):
        for j in range(heigth):
            cmds.append(f"setblock ~{i} ~-1 ~{j} bedrock")
    return cmds

def create_mosaic(img: np.ndarray, images_tuple, resolution=10, block_size=16, accuracy=40, saveto="output.png", ground=False, logs=False):
    if logs: print("Starting...")
    pixelated_img = img[::resolution,::resolution]
    images_array = images_tuple[0]
    images = images_tuple[1]
    filenames = images_tuple[2]
    commands = []
    #print(images_array.shape)
    #print(images_array[0])
    #print(np.apply_over_axes(np.mean, images_array, [1,2]))
    image_values = np.apply_over_axes(np.mean, images_array, [1,2]).reshape(len(images),3)
    if logs: print("Assigned color values to all images")
    tree = spatial.KDTree(image_values)
    if logs: print("Created Tree")
    target_res = pixelated_img.shape
    image_idx = np.zeros(target_res, dtype=np.uint32)
    if ground: commands += create_fill_commands(target_res[1], target_res[0])

    for i in range(target_res[0]):
        for j in range(target_res[1]):

            template = pixelated_img[i, j]
            if accuracy > len(images_array): accuracy=len(images)

            match = tree.query(template, k=accuracy)
            pick = randint(0, accuracy-1)
            image_idx[i, j] = match[1][pick]
    if logs: print("Chose images")

    canvas = Image.new("RGB", (block_size*target_res[1], block_size*target_res[0]-1))

    #print(target_res[0], target_res[1])
    for i in range(target_res[1]):
        for j in range(target_res[0]):
            #print(image_idx[j, i])
            arr = images[image_idx[j, i][0]]
            
            filename = filenames[image_idx[j, i][0]]
            commands.append(findindices.place(i, j, filename))
            
            x, y = i*block_size, j*block_size
            im = Image.fromarray(arr)
            canvas.paste(im, (x,y))
    
    canvas_array = np.asarray(canvas)
    canvas_array = canvas_array[..., ::-1]
    cv2.imwrite(saveto, canvas_array)
    #canvas.save(saveto)
    return commands
    if logs: print("Done")