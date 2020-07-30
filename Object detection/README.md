# All the Scripts That I used in Object detection are HERE!!

I used **`https://github.com/AlexeyAB/darknet`** for custom object detection.  
All scripts in this DIR are made to make my life easy using AlexeyAB's library!  

<hr>

**make_DB.py**: **`This script is used to make Database out of Images Dirs.`**  
<br>

**This is how you use it:**  
**`python make_DB.py -s <source> -d <destination>`**
<br>

source should be like:  
>source  
>>class1
>>>classes.txt
>>>img1.jpg
>>>img1.txt
>>> & so on...
>>class2
>> & so on...

output will be like:  
>destination
>>classes.txt
>>img1.jpg
>>img1.txt
>> & so on...

<hr>

**make_obj.py**: **`This script is used to make obj.data & obj.names out of Data base obtained out of make_DB.py.`**  
<br>

**This is how you use it:**  
**`python make_obj.py -d <data> -o <out> -p <percentage>`**
<br>

**`data`** contains the DataBase of Images such that it has two DIRs, `train` **ONLY!**.  

**`out`** will contain 4 files. `obj.name`, `obj.data`, `train.txt` & `test.txt`.  

**`percentage`** specifies how percentage split of images in `train` DIR.

<hr>

