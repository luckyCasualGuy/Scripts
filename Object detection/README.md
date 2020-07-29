# All the Scripts That I used in Object detection are HERE!!

I used **`https://github.com/AlexeyAB/darknet`** for custom object detection.  
All scripts in this DIR are made to make my life easy using AlexeyAB's library!  

<hr>

**make_DB.py**: This script is used to make Database out of Images.  
<br>
**This is how you use it:**  
`python make_DB.py -s <source> -d <destination>`
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