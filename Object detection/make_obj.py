from pathlib import Path
import argparse
from shutil import copy
from random import sample


def main(data, backup):
    # Required paths
    data = Path(data) #from user
    train = data / 'train'
    test = data / 'test'
    classes = train / 'classes.txt'
    out = Path('./obj')
    train_txt = out / 'train.txt'
    test_txt = out / 'test.txt'
    obj_names = out / 'obj.names'
    obj_data = out / 'obj.data'
    backup = Path(backup) # from user

    if not out.exists(): out.mkdir()

    #copying classes.txt to obj.names
    obj_names.unlink(missing_ok=True)
    copy(classes, obj_names)

    # Got the class value
    cls = len(classes.read_text().split('\n'))

    # run this script in the root folder!

    # making train & test txts
    train_imgs = list(train.glob('*.jpg'))
    test_imgs = list(test.glob('*.jpg'))

    train_txt.unlink(missing_ok=True)
    train_txt.write_text('\n'.join(map(str, train_imgs)))

    test_txt.unlink(missing_ok=True)
    test_txt.write_text('\n'.join(map(str, test_imgs)))

    write_text = "classes = {}\ntrain = {}\nvalid = {}\nnames = {}\nbackup = {}".format(
                    str(cls), str(train_txt), str(test_txt), str(obj_names), str(backup))

    obj_data.unlink(missing_ok=True)
    obj_data.write_text(write_text)

    print('Done! :)')

if __name__ == '__main__':
    # Parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', type=str, required=True, 
                        help="Path to folder containing train & test folders.")
    parser.add_argument('-o', '--out', type=str, required=True, 
                        help="Path to output folder.")
    args = parser.parse_args()

    main(args.data, args.out)