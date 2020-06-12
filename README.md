# CAPTCHA solver by Convolutional Neural Network


First, you need to download Tensorflow and the Tensorflow Object Detection API (you can use [these instructions](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md/).



Everytime you run an instance of this program from the command line, you need to navigate to `tensorflow/models/research/` and run the following command to append the directories to the appropriate path. (Haven't figured out how to edit the .bash file to fix this yet.) I put the /tensorflow folder in my `/~/` (Users) directory.

```
# From tensorflow/models/research/
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```

Then, I run the program as
```
python main_.py
```
