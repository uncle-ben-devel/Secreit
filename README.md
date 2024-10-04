# Deep learning-based classification of the mouse estrous cycle stages, K. Sano and etal, 2020, Scientific Reports.
https://www.nature.com/articles/s41598-020-68611-0

# SECREIT
Mouse Estrous Cycle Estimation

NOTE: This project is not related to the original research and authors. The only purpose of it is to make the original code more accessible by providing pre-built binaries.

## Running the code from the provided binaries (recommended)
- Download the latest binaries from the [releases](https://github.com/uncle-ben-devel/Secreit/releases/latest)
- The program can be run from the command line or via drag-and-drop of image files onto the main binary named ```secreit-cli```
- To check the available command line options, use ```-h``` or ```--help```

## Running the code from python
- Download the model from [here](https://opac.ll.chiba-u.jp/da/curator/108041/weights.hdf5) and put it into a folder named ```models``` within the root of the project (this folder)
- Install the environment from ```environment.yml``` using conda
```conda env create -f environment.yml```
- Activate it
```conda activate secreit-env```
- run the program
```python secreit-cli.py --help```

## Creating binaries
- Install the environment as like when running the code from python
- Activate it
- Run pyinstaller with the provided spec file ```secreit-cli.spec```
```pyinstaller secreit-cli.spec```
- You can now pick up the binaries from the ```dist/``` folder.

## Overview
![Overview](https://github.com/uncle-ben-devel/Secreit/blob/master/Example/Overview.png)

## Model AUC (Performance)
#### SECREIT correctly classified competitive to two professionals
#### diestrus stage (D): 0.982 
#### estrus stage (E): 0.979
#### proestrus stage (P): 0.962

## Dataset
### Example of file name
```D_a_14_e1_Auto2_train.png```
1. ```D ```: Estrous Stage. When the estrous stage is intermediate class, we described it using  ```_ ```, such as  ```D_E ```.
1. ```a_14_e1```: image id
1. ```Auto2```: Name of Experiment. ```Auto2``` and ```Auto3``` was used for trainig. ```Auto1``` was for validation and ```Auto4``` is for test. 
### Dataset download
- [Dataset D, Part 1](https://opac.ll.chiba-u.jp/da/curator/108041/D_part1.zip)
- [Dataset D, Part 2](https://opac.ll.chiba-u.jp/da/curator/108041/D_part2.zip)
- [Dataset D, Part 3](https://opac.ll.chiba-u.jp/da/curator/108041/D_part3.zip)
- [Dataset E](https://opac.ll.chiba-u.jp/da/curator/108041/E.zip)
- [Dataset P](https://opac.ll.chiba-u.jp/da/curator/108041/P.zip)