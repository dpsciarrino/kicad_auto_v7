import os

import constants as constants

def create_directory():
    # Create the default directory structure
    try:
        for folder in constants.FOLDERS:
            if not os.path.exists(folder):
                os.makedirs(folder)
    except Exception as e:
        return False
    
    # Create the BOM template
    with open('bom/bom_template.csv', 'w') as fd:
        print("Initializing BOM Template")
        fd.write("Item #,Designator,Qty.,Description,Manufacturer,Mfr Part Number")
        fd.close()
        print("Done")
      
    return True

def read_configuration():
    ctx = {
        "PROJECT_NAME": "kicad7_proj",
        "PROJECT_TITLE": "",
        "PROJECT_REVISION": "",
        "PROJECT_AUTHOR": "",
        "PROJECT_COMMENT1": "",
        "PROJECT_COMMENT2": "",
        "PROJECT_COMMENT3": "",
        "PROJECT_COMMENT4": "",
        "PROJECT_DATE": ""
    }

    # Open configuration file
    with open(constants.CONFIG_FILEPATH, 'r') as cfg_file:
        config_file_lines = cfg_file.read().split("\n")

        i = 0
        for cfg_line in config_file_lines:
            i += 1
            if cfg_line != "" and len(config_file_lines)>=i:
                key_value = cfg_line.split("=")
                key = key_value[0]
                value = key_value[1].replace("\"", "").replace("'", "")

                if key == "PROJECT_NAME" and value != "":
                    ctx['PROJECT_NAME'] = value
                elif key == "TITLE":
                    ctx['PROJECT_TITLE'] = value
                elif key == "REV":
                    ctx['PROJECT_REVISION'] = value
                elif key == "AUTHOR":
                    ctx["PROJECT_AUTHOR"] = value
                elif key == "COMMENT1":
                    ctx["PROJECT_COMMENT1"] = value
                elif key == "COMMENT2":
                    ctx['PROJECT_COMMENT2'] = value
                elif key == "COMMENT3":
                    ctx['PROJECT_COMMENT3'] = value
                elif key == "COMMENT4":
                    ctx['PROJECT_COMMENT4'] = value
                else:
                    ctx['PROJECT_DATE'] = constants.TODAY_DATE
        
        cfg_file.close()
    
    return ctx

def build_eeschema(cfg: dict):
    if not os.path.exists(constants.SCH_FILE):
        raise FileNotFoundError(f"Cannot find EESchema file: {constants.SCH_FILE}")
    
    print("Configuring EESchema file...")

    try:
        with open(constants.SCH_FILE, 'r+') as sch_file:
            sch_contents = sch_file.read()

            sch_contents = sch_contents.replace("{TITLE}", cfg['PROJECT_TITLE'])
            sch_contents = sch_contents.replace("{REVISION}", cfg['PROJECT_REVISION'])
            sch_contents = sch_contents.replace("{AUTHOR}", cfg['PROJECT_AUTHOR'])
            sch_contents = sch_contents.replace("{COMMENT 1}", cfg['PROJECT_COMMENT1'])
            sch_contents = sch_contents.replace("{COMMENT 2}", cfg['PROJECT_COMMENT2'])
            sch_contents = sch_contents.replace("{COMMENT 3}", cfg['PROJECT_COMMENT3'])
            sch_contents = sch_contents.replace("{COMMENT 4}", cfg['PROJECT_COMMENT4'])
            sch_contents = sch_contents.replace("{DATE}", cfg['PROJECT_DATE'])
            
            # Prevent file edit while in development mode
            if not constants.DEV_MODE:
                sch_file.seek(0)
                sch_file.truncate(0)
                sch_file.write(sch_contents)
            
            sch_file.close()
    except Exception as e:
        print("Error in EESchema configuration: ", e.args)
        return -1
        
    print("Done configuring schematic file.")

    return 0

def build_pcbnew(cfg: dict):
    if not os.path.exists(constants.PCB_FILE):
        raise FileNotFoundError(f"Cannot find PCBNew file: {constants.PCB_FILE}")
    
    print("Configuring PCBNew file...")
    try:
        with open(constants.PCB_FILE, 'r+') as pcb_file:
                pcb_contents = pcb_file.read()
                pcb_contents = pcb_contents.replace("{TITLE}", cfg['PROJECT_TITLE'])
                pcb_contents = pcb_contents.replace("{DATE}", cfg['PROJECT_DATE'])
                pcb_contents = pcb_contents.replace("{REVISION}", cfg['PROJECT_REVISION'])
                pcb_contents = pcb_contents.replace("{AUTHOR}", cfg['PROJECT_AUTHOR'])
                pcb_contents = pcb_contents.replace("{COMMENT 1}", cfg['PROJECT_COMMENT1'])
                pcb_contents = pcb_contents.replace("{COMMENT 2}", cfg['PROJECT_COMMENT2'])
                pcb_contents = pcb_contents.replace("{COMMENT 3}", cfg['PROJECT_COMMENT3'])
                pcb_contents = pcb_contents.replace("{COMMENT 4}", cfg['PROJECT_COMMENT4'])
                
                if not constants.DEV_MODE:
                    pcb_file.seek(0)
                    pcb_file.truncate(0)
                    pcb_file.write(pcb_contents)

                pcb_file.close()
            
    except Exception as e:
        print("Error in PCBNew configuration: ", e.args)
        return -1
        
    print("Done configuring PCBNew file.")

    return 0

def rename_project_files(cfg: dict):
    print("Renaming project files...")
    with open(constants.PRL_FILE, 'r+') as prl_file:
        prl_contents = prl_file.read()

        prl_contents = prl_contents.replace("{PROJECT_NAME}", cfg['PROJECT_NAME'])
        
        if not constants.DEV_MODE:
            prl_file.seek(0)
            prl_file.truncate(0)
            prl_file.write(prl_contents)

        prl_file.close()
    
    with open(constants.PRO_FILE, 'r+') as pro_file:
        pro_contents = pro_file.read()

        pro_contents = pro_contents.replace("{PROJECT_NAME}", cfg['PROJECT_NAME'])
        
        if not constants.DEV_MODE:
            pro_file.seek(0)
            pro_file.truncate(0)
            pro_file.write(pro_contents)

        pro_file.close()
        
    for f in os.listdir(constants.KICAD7_DIR):
        if f[:11] == "kicad7_proj":
            fsplit = f.split(".")
            newName = os.path.join(constants.KICAD7_DIR, cfg['PROJECT_NAME'] + "." + fsplit[1])
            
            print(newName)
            if not constants.DEV_MODE:
                try:
                    os.rename(os.path.join(constants.KICAD7_DIR, f), newName)
                    print("Renamed:\nOLD:", os.path.join(constants.KICAD7_DIR, f), "\nNEW:", newName)
                except Exception as e:
                    print("Exception:", e)
    
    print("Done renaming project files")

def build_libraries(cfg):
    print("Building library files...")
    with open(constants.SYM_LIB_TABLE, 'r+') as slt_file:
        slt_contents = slt_file.read()

        slt_contents = slt_contents.replace("{PROJECT_NAME}", cfg['PROJECT_NAME'])
        slt_contents = slt_contents.replace("descr \"\"", f"descr \"{cfg['PROJECT_NAME']} Symbol Library\"")

        if not constants.DEV_MODE:
            slt_file.seek(0)
            slt_file.truncate(0)
            slt_file.write(slt_contents)

        slt_file.close()
    
    with open(constants.FP_LIB_TABLE, 'r+') as flt_file:
        flt_contents = flt_file.read()

        flt_contents = flt_contents.replace("{PROJECT_NAME}", cfg['PROJECT_NAME'])
        slt_contents = flt_contents.replace("descr \"\"", f"descr \"{cfg['PROJECT_NAME']} Footprint Library\"")

        if not constants.DEV_MODE:
            flt_file.seek(0)
            flt_file.truncate(0)
            flt_file.write(flt_contents)

        flt_file.close()
    
    print("Renaming symbols library files...")
    for f in os.listdir(constants.SYMBOLS_LIB_DIR):
        if f[:11] == "kicad7_proj":
            fsplit = f.split(".")
            newName = os.path.join(constants.SYMBOLS_LIB_DIR, cfg['PROJECT_NAME'] + "." + fsplit[1])

            if not constants.DEV_MODE:
                try:
                    os.rename(os.path.join(constants.SYMBOLS_LIB_DIR, f), newName)
                    print("Renamed:\nOLD:", os.path.join(constants.SYMBOLS_LIB_DIR, f), "\nNEW:", newName)
                except Exception as e:
                    print("Exception:", e)
    print("Done")
    print("Renaming .pretty folder...")
    try:
        newPrettyDir = constants.PRETTY_DIR.replace("kicad7_proj.pretty", f"{cfg['PROJECT_NAME']}.pretty")

        if not constants.DEV_MODE:
            os.rename(constants.PRETTY_DIR, newPrettyDir)
            print("Renamed:\nOLD:", constants.PRETTY_DIR, "\nNEW:", newPrettyDir)
            
    except Exception as e:
        print("Exception:", e)
    print("Done")
    


def build():
    # Can't build without configuration file
    if not os.path.exists("config.txt"):
        raise Exception("Run configuration first.")

    # Create project directory
    # Prevent directory build while in development mode
    if (not constants.DEV_MODE) and (not create_directory()):
       print("Error in directory creation.")
    
    # Initialize project variables
    cfg = read_configuration()

    build_eeschema(cfg)

    build_pcbnew(cfg)

    rename_project_files(cfg)

    build_libraries(cfg)



