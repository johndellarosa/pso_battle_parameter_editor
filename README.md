# PSO Battle Parameter Editor

## Using the library

### Installing
* The simplest way is to download the .py file and place it in the same directory as the file you wish to use, such as a Jupyter notebook or another .py file
* You can import the file by using `import PSO_Battle_Parameter_Editor as pso` to import it with alias `pso`



### Loading Data
Data is loaded and manipulated using the Table class. This can be done by by calling the Table constructor which takes two arguments:
1. Battle parameter file location
2. Episode number (1,2,4)
An example is:
```file = pso.Table('BattleParamEntry.dat',episode=1)```

### Viewing Data
There are 4 main sections to the file:
1. Stats Data
2. Attack Data
3. Resist Data
4. Movement Data

#### Stats+Resist
To get the most well-documented values in a neat table, there is the `get_merged_table` method, which takes the following parameters:
1. Difficulty (int): 0 for normal; 1 for hard; 2 for very hard; 3 for ultimate.
2. Verbose (bool, optional): Prints everything while parsing

Sample use:
```file.get_merged_table(difficulty=0)```

### Modifying Data

#### Modifying Stats
```set_stat_property(self, value, stat, enemy, difficulty)```
#### Modifying Resist 
```set_resist_property(self, value, stat, enemy, difficulty)```

### Finalizing Changes
To avoid potentially ruining game files, there are some safeguards. The relevant method is `write` which has the following parameters:
1. new_file_name: the file name that the modified data will be exported as. The library will not modify the read-in file unless you choose for this parameter to be the same name.
2. overwrite (optional with default False): if there already exists a file with the chosen name, the method will warn you that a file with that name already exists and not write out the data. If you wish to allow overwriting the file, you can set overwrite=True.
Sample use:
```file.write('test_param.dat')```

## Acknowledgements

Code by John Della Rosa

File information based on [Newserv/fu](https://github.com/fuzziqersoftware/newserv)https://github.com/fuzziqersoftware/newserv

Inspired by Solybum
