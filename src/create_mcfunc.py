import shutil
import os

def create_functions(commands):
    chunks = []
    if len(commands) > 10000:
        print("creating chunks")
        for i in range(len(commands)//10000):
            chunks.append(commands[i*10000:(i+1)*10000])
            #print(f"created chunk {i+1} out of {len(commands)//10000}")
        chunks.append(commands[((len(commands)//10000)*10000):((len(commands)//10000)*10000+len(commands)%10000)])
        #print(f"appending last chunk: {commands[((len(commands)//10000)*10000):((len(commands)//10000)*10000+len(commands)%10000)]}")
        print(f"created {len(commands)//10000} chunks with 10000 commands")
        for i,chunk in enumerate(chunks):
            with open(f"temp/data/image/functions/chunks/{i}.mcfunction", "w") as file:
                for command in chunk:
                    file.write(f"{command}\n")
        with open("temp/data/image/functions/build.mcfunction", "w") as file:
            for i in range(len(chunks)):
                file.write(f"function image:chunks/{i}\n")
    else:
        with open("temp/data/image/functions/build.mcfunction", "w") as file:
            for command in commands:
                    file.write(f"{command}\n")

def create_datapack(commands, desc=""):
    with open("temp/pack.mcmeta", "w") as mcmeta:
        mcmeta.write('{"pack": {"pack_format": 26,"description": "{' + desc + '}"}}')
    if os.path.exists("temp/data"):
        shutil.rmtree("temp/data")
    os.makedirs("temp/data/image/functions/chunks")
    create_functions(commands)
    shutil.make_archive("image", "zip", "temp")
    shutil.rmtree("temp/data")
    os.remove("temp/pack.mcmeta")

