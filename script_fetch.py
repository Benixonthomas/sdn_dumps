

import datetime
import subprocess
import time
import os 

def log_script_output(script_path, log_file_path):

    with open(log_file_path, 'w') as log_file:

        print("Starting the controller....")
	time.sleep(5)
	try:

            # Run the script and redirect stdout and stderr to the log file

            subprocess.call(["python", script_path], stdout=log_file, stderr=subprocess.STDOUT)

        except Exception as e:

            # Handle any exceptions that might occur

            log_file.write( str(e))
    print("Executing and fetching the details.....")
    os.popen("sudo chown student: {}".format(log_file_path))
    os.popen("chmod 777 {}".format(log_file_path))
 

if __name__ == "__main__":

    # Replace 'your_script.py' with the actual path to your script

    script_to_run = "/home/student/git_repo/sdn_dumps/topo_script.py"

    dt_nw=datetime.datetime.now()
    fr_dt=dt_nw.strftime("%Y%m%d%H%M%S") 

    # Specify the path for the log file

    log_file_path = "/home/student/git_repo/sdn_dumps/dumps/mininetdump_{}.log".format(fr_dt)

   

    # Log the output of the script to the specified file

    log_script_output(script_to_run, log_file_path)
