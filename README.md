# How to use
* Install Python (If you don't have Python installed already)
  * 64-bit: https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe
  * 32-bit: https://www.python.org/ftp/python/3.10.5/python-3.10.5.exe
  * After downloading the file, execute the file to install Python
* Download the code as zip archive by clicking on the green "Code" button and then clicking "Download ZIP"
* Extract the zip archive
* Open the folder and run app.py
* The program will ask you for a few parameters. Here is the description for each one:
  * Resolution: The Image will be scaled down to (1/resolution)*original size, which means lower inputs result in a better quality (and a longer waiting time)
  * Accuracy: Defines how much the blocks can vary. 2 is minimum. Higher inputs result in a noisy looking image.
  * No Light sources: In some cases light sources can look bad/weird so check this box if you don't want light sources in your image
  * No shulker boxes: Shulker boxes won't get rendered if you are a certain distance away so you can disable them too
  * No gravity blocks: Gravity affected blocks won't be used if checked
  * Supporting bedrock area: Creates a bedrock area below your image to support gravity affected blocks
  * **If the Submit button doesn't work check if:**
    * You're inputs for Resolution and Accuracy are valid (must be integers, Resolution can't be lower than 1, Accuracy can't be lower than 2)
    * If you leave the inputs for Resolution and Accuracy empty, the program will use the default values (Resolution: 20, Accuracy: 3)
* After pressing Submit you will have to select an image (the program will stop if you press cancel or the X)
* The program will process your request and after a while (How long it takes depends on your resolution and the size of the image, Only takes a few seconds to a minute in most cases)
* When the program finished it will tell you where the datapack is saved
* Put the datapack in the datapacks folder of your Minecraft world (%appdata%/.minecraft/saves/[YOUR WORLD NAME]/datapacks
* Reload your World or Join your world if you are not in the world
* Execute the command `/function image:build` (WARNING: Any blocks in the area where the image will be placed will be REPLACED by the image, so either make a backup or clear the area)
If only parts of the image get generated try executing following command: `/gamerule maxCommandChainLength 999999999`
