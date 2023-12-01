## KiCad Auto v7

KiCad Auto v7 is a semi-automatic build tool for instantiating KiCad projects. The tool takes in some basic project parameters from command line inputs, configures a title block, and creates a usable directory structure for a KiCad v7 project.

**NOTE:** *THIS HAS ONLY BEEN TESTED WITH THE FOLLOWING KICAD/OS VERSIONS:*
- KiCad Version: 7.0.9
- Platform: Windows 11 Home

### Usage with Python

Clone the repo using `git clone ...`. The directory structure that results looks like the following tree:

```
.
├── kicad_proj
│   ├── fp-lib-table
│   ├── libs
│   │   ├── footprints
│   │   │   └── kicad7_proj.pretty
│   │   ├── models
│   │   └── symbols
│   │       └── kicad7_proj.kicad_sym
│   ├── meta
│   │   └── info.html
│   ├── sym-lib-table
│   ├── kicad7_proj.kicad_pcb
│   ├── kicad7_proj.kicad_prl
│   ├── kicad7_proj.kicad_pro
│   ├── kicad7_proj.kicad_sch
│   └── title_block_v7.kicad_wks
├── kicad7_proj.py
├── makefile
└── README.md
```

To configure the project, run the command:

```
python kicad7_project.py config
```

![](https://github.com/dpsciarrino/kicad_auto_v7/blob/main/KiCAD%20v7%20Configuration.gif)

You will prompted for some basic configuration parameters. What is entered will populate a file called `config.txt` which is generated after the command finished. The following parameters are needed:

1.  Project Name
    - Give your project a specific name. This will be what .pro and other associated project files will be called.
2.  Sheet 1 Title
    - A title for your project. Maps to "Comment1" on title block.
3.  Sheet 1 Subtitle
    - A brief descriptive subtitle. Maps to "Comment2" on title block.
4.  Project Revision
    - The revision of your project.
5.  Author
    - Author, organization, or company name. Appears in large text at the bottom of the title block.

Once the configuration parameters are populated, review the associated `config.txt` file.

After reviewing the `config.txt` file, run the following line of code. This will build the final directory structure and modify the corresponding KiCAD files.

```
python kicad7_project.py build
```

A successful run will result in a directory structure similar to below:

```
.
├── assembly_outputs
├── bom
│   └── bom_template.csv
├── config.txt
├── datasheets
├── docs
├── fab_outputs
├── freecad_outputs
├── images
├── kicad7_proj
│   ├── fp-lib-table
│   ├── libs
│   │   ├── footprints
│   │   │   └── proj-id.pretty
│   │   ├── models
│   │   └── symbols
│   │       └── proj-id.kicad_sym
│   ├── proj-id.pcb
│   ├── proj-id.pro
│   ├── proj-id.sch
│   ├── proj-id.prl
│   ├── sym-lib-table
│   └── title_block_v7.kicad_wks
├── kicad7_proj.py
├── makefile
├── pdf_outputs
├── README.md
├── simulation
└── software
```

### Usage with Make

You can also run the program using Make. Use the following to run project configuration:

```
make config
```

Then, build the project using:
```
make project
```

* * *

## Features

### Project Specific Libraries

Empty libraries for component symbols and footprints are automatically created and ready to use.

### Directory Structure

A ready-to-use directory structure is generated, able to carry beginner to intermediate (possibly even advanced!) KiCAD projects.

### BOM CSV

A basic CSV file is created with pre-defined headers corresponding to useful BOM fields. Open it with your favorite spreadsheet editor to manually track BOM items.

* * *

## Directory Structure

### Assembly Outputs

Pertinent files for assembly.

### BOM

Anything related to bill of materials.

### Datasheets

For storing datasheets.

### Docs

Documents that are specific to this project. Manuals, Diagrams, etc.

### Fab Outputs

For storing GERBERS and drill files.

### Freecad Outputs

For anything related to FreeCAD (may change in future version).

### Images

Images specific to this project.

### KiCAD Project

The entire KiCAD project sits in this directory (with the exception of global configuration and global library files).

### PDF Outputs

PDF drawings specific to this project, exported from either KiCAD or FreeCAD.

### Simulation

Stores simulation files. Circuit simulation, heat transfer, etc.

### Software

In case you need to program anything, here's a folder for software.

* * *
