import os, sys, subprocess, psutil, shutil

################################################################

# VARIABLES AND ETC.

################################################################

temp_path = os.environ.get("Temp")


################################################################

# FUNCTIONS

################################################################


def error_handler(errortype, item, error):
    pass


def clear_tmp():
    print("Clearing Temp...")
    for item in os.listdir(temp_path):
        item_path = os.path.join(temp_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            print(e)
            error_handler("delete_er", item, e)
