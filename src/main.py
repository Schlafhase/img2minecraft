import cv2
from src import mc_imgmosaic
import tkinter as tk
from tkinter import filedialog as fd
from src.create_mcfunc import create_datapack, create_functions
import os

mc_filepath = "./mctextures"
saveto = "./outputs"
root = tk.Tk()


canvas = tk.Canvas(root, width=400, height=220)
canvas.pack()

shulkers = ["yellow_shulker_box.png", "white_shulker_box.png", "shulker_box.png", "red_shulker_box.png", "purple_shulker_box.png", "pink_shulker_box.png", "orange_shulker_box.png", "magenta_shulker_box.png", "lime_shulker_box.png", "light_gray_shulker_box.png", "light_blue_shulker_box.png","green_shulker_box.png", "gray_shulker_box.png", "cyan_shulker_box.png", "brown_shulker_box.png", "blue__shulker_box.png", "black_shulker_box.png"]
light_sources = ["glowstone.png", "enchanting_table_top.png", "sea_lantern.png", "jack_o_lantern.png", "verdant_froglight_top.png", "pearlescent_froglight_top.png", "ochre_froglight_top.png", "shroomlight.png", "beacon.png", "crying_obsidian.png"]
gravity_blocks = ["sand.png", "gravel.png", "yellow_concrete_powder.png", "white_concrete_powder.png", "red_concrete_powder.png", "purple_concrete_powder.png", "pink_concrete_powder.png", "orange_concrete_powder.png", "magenta_concrete_powder.png", "lime_concrete_powder.png", "light_gray_concrete_powder.png", "light_blue_concrete_powder.png", "green_concrete_powder.png", "gray_concrete_powder.png", "cyan_concrete_powder.png", "brown_concrete_powder.png", "blue_concrete_powder.png", "black_concrete_powder.png"]
blacklist = []

res = 20
acc = 3
no_light_sources = tk.IntVar()
no_shulkers = tk.IntVar()
ground = tk.BooleanVar()
no_gravity_blocks = tk.IntVar()

res_entry = tk.Entry(root)
res_label = tk.Label(root, text="Resolution (lower numbers = better resolution, 1 is min)")
acc_entry = tk.Entry(root)
acc_label = tk.Label(root, text="Accuracy/Randomness (lower number = less randomness, 2 is min)")
canvas.create_window(200, 40, window=res_entry)
canvas.create_window(200, 20, window=res_label)
canvas.create_window(200, 80, window=acc_entry)
canvas.create_window(200, 60, window=acc_label)

def submit():
    global res, acc, blacklist
    if no_light_sources.get() == 1:
        #print("No light sources")
        blacklist += light_sources
    if no_shulkers.get() == 1:
        #print("No shulkers")
        blacklist += shulkers
    if no_gravity_blocks == 1:
        #print("No gravity blocks")
        blacklist += gravity_blocks
    try:
        res = int(res_entry.get())
        acc = int(acc_entry.get())
    except:
        print("Resolution and Accuracy must be Integers")
        return
    if res < 1 or acc < 2:
        print("Resolution must be at least 1 and Accuracy must be at least 2")
        return
    print(f"No Shulkers: {bool(no_shulkers.get())}, No Light sources: {bool(no_light_sources.get())}, No gravity blocks: {bool(no_gravity_blocks.get())}, Create ground: {ground.get()}")
    print(f"Resolution: {res}, Accuracy: {acc}")
    root.destroy()

submit_button = tk.Button(text="Submit", command=submit)
no_light_box = tk.Checkbutton(root, text="Don't use Light sources", variable=no_light_sources)
no_shulkers_box = tk.Checkbutton(root, text="Don't use Shulker boxes", variable=no_shulkers)
gravity_blocks_box = tk.Checkbutton(root, text="Don't use gravity affected blocks", variable=no_gravity_blocks)
ground_box = tk.Checkbutton(root, text="Create bedrock area below (to support gravity affected blocks)", variable=ground)
canvas.create_window(200, 205, window=submit_button)
canvas.create_window(200, 120, window=no_light_box)
canvas.create_window(200, 140, window=no_shulkers_box)
canvas.create_window(200, 160, window=gravity_blocks_box)
canvas.create_window(200, 180, window=ground_box)

root.mainloop()

mc_images = mc_imgmosaic.create_img_array(images_filepath=mc_filepath, img_size=16, blacklist=blacklist)
im = cv2.imread(fd.askopenfilename(filetypes=[("Image files", "*.png *.jpg")]))
im = im[..., ::-1]

commands = mc_imgmosaic.create_mosaic(img=im, images_tuple=mc_images, resolution=res, block_size=16, accuracy=acc, logs=True, saveto="./outputs/preview.png", ground=ground.get())
print(f"Using {len(commands)} blocks")
with open("./outputs/debug.txt", "w") as file:
    file.write(str(commands))
create_datapack(commands=commands, desc="Image datapack")
print()
print(f"You're datapack is saved at {os.getcwd()}\image.zip")
print(f"You can see a preview of the image at {os.getcwd()}\outputs\preview.png")
print("Put it in the datapacks folder of your Minecraft world and run the following command in your Minecraft world:\n/function image:build")
input("Press Enter to close")
