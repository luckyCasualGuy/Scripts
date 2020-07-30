from pathlib import Path
import argparse
from shutil import copy
from random import sample


def main(data_dir, backup_dir, percentage):
   # temperory:
    data = Path(data_dir) #from user
    classes = data / 'classes.txt'
    out = Path('./obj')
    train_txt = out / 'train.txt'
    test_txt = out / 'test.txt'
    obj_names = out / 'obj.names'
    obj_data = out / 'obj.data'
    backup = Path(backup_dir) # from user

    out.mkdir(exist_ok=True)

    #copying classes.txt to obj.names
    obj_names.unlink(missing_ok=True)
    copy(classes, obj_names)

    # Got the class value
    clss = len(classes.read_text().split('\n'))

    all_imgs = list(data.glob("*.jpg"))
    # run this script in the root folder!
    all_imgs = sample(all_imgs, len(all_imgs))

    # percentage split
    percent = percentage # from user
    percent /= 100
    split_at = int(len(all_imgs) * percent) #141 #126 #15

    # output checked
    train_imgs = all_imgs[:split_at]
    test_imgs = all_imgs[split_at:]

    # making train & test txts

    train_txt.unlink(missing_ok=True)
    train_txt.write_text('\n'.join(map(str, train_imgs)))

    test_txt.unlink(missing_ok=True)
    test_txt.write_text('\n'.join(map(str, test_imgs)))

    write_text = "classes = {}\ntrain = {}\nvalid = {}\nnames = {}\nbackup = {}".format(
                    str(clss), str(train_txt.absolute()), 
                    str(test_txt.absolute()), str(obj_names.absolute()), 
                    str(backup.absolute()))

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
    parser.add_argument('-p', '--percent', type=int, required=True, 
                    help="Percent split your dataset.")
    args = parser.parse_args()

    main(args.data, args.out, args.percent)