import shutil
import os
import sys
import subprocess
Import("env")


def move_file(source, target, env):
    # get the source file path and name
    file_path = target[0].get_abspath()
    file_name = os.path.basename(file_path)
    
    # get the device target from the environment
    device_target = env.GetProjectOption("device_label")
    print(device_target)

    # check the operating system and create the destination file path accordingly
    if os.name == "nt":  # Windows
        # check if the 'pywin32' module is installed and install it if not
        try:
            import win32api
        except ImportError:
            print("The 'pywin32' module is not installed. Installing now...")
            import subprocess
            subprocess.call([sys.executable, "-m", "pip", "install", "pywin32"])
            import win32api

        # get a list of all mounted volumes using the win32api module
        volumes = win32api.GetLogicalDriveStrings()
        volumes = volumes.split('\x00')[:-1]

        # loop over the mounted volumes and look for a volume with the correct label
        destination_found = False
        for volume in volumes:
            try:
                label = win32api.GetVolumeInformation(volume)[0]
            except:
                # skip this volume if there is an error accessing the label
                continue

            if label == device_target:
                # create the destination file path by joining the volume and the file name
                destination_file_path = os.path.join(volume, file_name)
                destination_found = True
                shutil.copy2(file_path, destination_file_path)
                output = f"The hexfile has been copied to '{destination_file_path}'"
                print(output)

        if not destination_found:
            output = f"Could not find a volume with the label '{device_target}'"
            print(output)
            exit()

    else:  # Linux
        # create the destination file path by joining the mount point and the file name
        destination_file_path = os.path.join("/media/", os.getlogin(), device_target, file_name)
        shutil.copy2(file_path, destination_file_path)
        output = f"The hexfile has been copied to '{destination_file_path}'"
        print(output)


env.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", move_file)
