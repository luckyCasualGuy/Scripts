from pathlib import Path
from shutil import copyfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--src', type=str, required=True, help="Source path")
parser.add_argument('-d', '--dst', type=str, required=True, help="Destination path")
args = parser.parse_args()

final = Path(args.dst)
p = Path(args.src)

final.mkdir(exist_ok=True)

img_dirs = [x for x in p.iterdir() if p.is_dir()]
classes = []

for i, dirs in enumerate(img_dirs, 0):
    
    clss = dirs / 'classes.txt'
    classes.append(clss.read_text())
    
    imgs = sorted(dirs.glob("[!classes]*.txt")) 
    for img in imgs: img.write_text(img.read_text().replace('0 ', str(i)+' '))
        
    imgs = sorted(dirs.glob("[!classes]*.*"))
    for img in imgs: copyfile(img, final / img.parts[-1])

clss = final / 'classes.txt'
write_str = ''.join(classes)
with clss.open(mode='w+') as f:
    f.write(write_str)
    f.close()

