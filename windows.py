import os, sys, subprocess, psutil, shutil

################################################################

# VARIABLES AND ETC.

################################################################

temp_path = os.environ.get("Temp")
recycle_path = os.environ.get("$Recycle.Bin")


################################################################

# FUNCTIONS

################################################################


def clear_tmp():
    for item in os.listdir(temp_path):
        item_path = os.path.join(temp_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            print(e)


def sfc_scannow():
    try:
        os.system("sfc /scannow")
    except Exception as e:
        print(e)


def clear_recyclebin():
    for item in os.listdir(recycle_path):
        item_path = os.path.join(temp_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            print(e)
