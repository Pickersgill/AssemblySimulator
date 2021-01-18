# Six Instruction Code Assembler and Simulator

## Quickstart:
To run the simulator on GCD algorithm use:

```python3 simulator gcd.mc -v```

This will run the GCD code in verbose mode and then print the entire memory contents, as well as
the memory contents of each variable.


## Usage:

### Assembler:
To use the assembler pass assembler.py a single argument as the source file.
The assembler will output the translated file contents. The source file should be
written in accordance with the format defined below.

### Simulator:
The simulator also takes a single positional argument as the source file, this can either be an 
already translated file or an untranslated assembly file. The simulator also has a couple of optional
arguments, use ```simulator -h ``` for help with these.

## Format
The input source file format differs slightly from the specification given. There can be no empty lines
and each instruction must be " " space deliniated:

```set variable 10```

See the .mc (machine code) files for further examples.
