# Deep learning-based classification of the mouse estrous cycle stages, K. Sano and etal, 2020, Scientific Reports.
https://www.nature.com/articles/s41598-020-68611-0

# SECREIT
Mouse Estrous Cycle Estimation

NOTE: This project is not related to the original research and authors. The only purpose of it is to make the original code more accessible by providing pre-built binaries.

## Running the code from the provided binaries (recommended)
- Download the latest binary from the releases tab
- The program can be run from the command line or via drag-and-drop of image files onto the main binary named ```secreit-cli```

## Running the code from python
- Download the model from [here](https://opac.ll.chiba-u.jp/da/curator/108041/weights.hdf5) and put it into a folder named ```models``` within the root of the project (this folder)
- Install the environment from ```environment.yml``` using conda
- Activate it
- ```secreit-cli.py``` is the main program to run

## Creating binaries
- Install the environment as specified in environment.yml using conda
- Activate it
- Run pyinstaller with the provided spec file ```secreit-cli.spec```

## Overview
![Overview](https://github.com/SanoKyohei/Secreit/blob/master/Example/Overview.png)  

## Model AUC (Performance)
#### SECREIT correctly classified competitive to two professionals
#### diestrus stage (D): 0.982 
#### estrus stage (E): 0.979
#### proestrus stage (P): 0.962

## Weight parameter
https://opac.ll.chiba-u.jp/da/curator/108041/weights.hdf5

## Dataset
### Example of file name
 "D_a_14_e1_Auto2_train.png" 
 <br> ①　D: Estrous Stage. When the estrous stage is intermediate class, we described it using "_", such as "D_E".
 <br> ②　a_14_e1: image id
 <br> ③　Auto2: Name of Experiment. Auto2 and Auto3 was used for trainig. Auto1 was for validation and Auto4 is for test. 
### Dataset download
<br> https://opac.ll.chiba-u.jp/da/curator/108041/D_part1.zip  <br> 
<br> https://opac.ll.chiba-u.jp/da/curator/108041/D_part2.zip <br> 
<br> https://opac.ll.chiba-u.jp/da/curator/108041/D_part3.zip  <br>
<br> https://opac.ll.chiba-u.jp/da/curator/108041/E.zip <br>
<br> https://opac.ll.chiba-u.jp/da/curator/108041/P.zip <br>



