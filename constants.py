from datetime import datetime
import os

CONFIG_FILE = "config.txt"

TODAY_DATE = datetime.today().strftime('%Y-%m-%d')

FOLDERS = [
    "assembly_outputs",
    "bom",
    "datasheets",
    "docs",
    "fab_outputs",
    "frecad_outputs",
    "images",
    "pdf_outputs",
    "simulation",
    "software"
]

# Working Directory
PWD = os.path.dirname(os.path.realpath(__file__))

# Config File
CONFIG_FILEPATH = os.path.join(PWD, "config.txt")

# KiCAD 7 Project Folders
KICAD7_DIR = os.path.join(PWD, "kicad7_proj/")
PRO_FILE = os.path.join(KICAD7_DIR, "kicad7_proj.kicad_pro")
PRL_FILE = os.path.join(KICAD7_DIR, "kicad7_proj.kicad_prl")
PCB_FILE = os.path.join(KICAD7_DIR, "kicad7_proj.kicad_pcb")
SCH_FILE = os.path.join(KICAD7_DIR, "kicad7_proj.kicad_sch")

SYMBOLS_LIB_DIR = os.path.join(KICAD7_DIR, "libs/symbols/")
FOOTPRINTS_LIB_DIR = os.path.join(KICAD7_DIR, "libs/footprints/")
MODELS_LIB_DIR = os.path.join(KICAD7_DIR, "libs/models/")
SYM_LIB_TABLE = os.path.join(KICAD7_DIR, "sym-lib-table")
FP_LIB_TABLE = os.path.join(KICAD7_DIR, "fp-lib-table")
PRETTY_DIR = os.path.join(FOOTPRINTS_LIB_DIR, "kicad7_proj.pretty")

DEV_MODE = False