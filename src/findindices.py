not_logs = ["command_block", "piston", "observer", "dispenser", "dropper", "barrel"]

def return_block_idx(blockname: str):
    log = True
    top = False
    bott = False
    side = False
    front = False
    back = False
    for name in not_logs:
        if name in blockname:
            log = False
            break
    if blockname.endswith("_top"): top = True
    elif blockname.endswith("_bottom"): bott = True
    elif blockname.endswith("_side"): side = True
    elif blockname.endswith("_front"): front = True
    elif blockname.endswith("_back"): back = True

    if log:
        if top: return blockname.split('_top')[0]
        if blockname.endswith("_log"): return f"{blockname}[axis=x]"
        elif side: return f"{blockname.split('_side')[0]}[axis=x]"
        else: return blockname
    else:
        if top: return f"{blockname.split('_top')[0]}[facing=up]"
        elif bott: return  f"{blockname.split('_bottom')[0]}[facing=down]"
        elif side: return f"{blockname.split('_side')[0]}[facing=north]"
        elif front: return f"{blockname.split('_front')[0]}[facing=up]"
        elif back: return f"{blockname.split('_back')[0]}[facing=down]"
    return blockname

def place(x, y, filename):
    blockname = filename.split(".")[0]
    block_idx = return_block_idx(blockname)
    command = f"setblock ~{x} ~ ~{y} {block_idx}"
    return command