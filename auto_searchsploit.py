#!/usr/bin/env python
import subprocess
import argparse
import os
import sys

# Python 2 and 3 compatibility
try:
    input = raw_input
except NameError:
    pass

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('kernel_version',
                    metavar='kernel_version',
                    type=str,
                    help='Kernel Version')

args = parser.parse_args()
kern_ver = args.kernel_version

# You can tellThis search is very specific to Linux Local Privelege Escalation
SEARCH = "searchsploit linux %s | grep local | grep -i privilege" % kern_ver
try:
    search_results = subprocess.check_output(SEARCH, shell=True)
except subprocess.CalledProcessError as grepexc:
    print("[-] No potential exploit found. Aborting...")
    exit(1)

base_dir = "/usr/share/exploitdb/platforms/linux/local"
dir_location = "%s/linux_%s/" % (os.environ['PWD'], kern_ver)

print("[*]Potential Exploit :")

print(search_results.decode())

search_results = search_results.strip().split(b"\n")

# try to copy to local directory first
file_list = [result.split(b"/")[-1] for result in search_results]

print("[*] File destination directory name: %s/linux_%s" %
      (os.environ["PWD"], kern_ver))

download_ans = input("[*] Do you want to download exploit file to "
                     "directory described above? [y/n]")
if download_ans.lower() == "y":
    new_dir = "mkdir %s" % (dir_location)
    # Make dir if not exist
    if not (os.path.isdir(dir_location)):
        subprocess.call(new_dir, shell=True)
    for _file in file_list:
        DOWNLOAD = "cp %s/%s %s" % (base_dir, _file, dir_location)
        subprocess.call(DOWNLOAD, shell=True)
    print("[+] All file downloaded in", dir_location)
else:
    print("[-] Exiting...")
    sys.exit(0)

# Now try to compile them if it is C
if 'c' in [file.split(b".")[1].lower() for file in file_list]:
    print("[*] C script found")
    print("[*] Compile format: gcc C_SCRIPT -o C_SCRIPT.exe")
    compile_ans = input(
        "[*] Do you want to compile the downloaded C script?"
        "(No Gurantee Success) [y/n]")
    if compile_ans.lower() == "y":
        success_exe = 0
        c_file_count = 0
        for _file in file_list:
            file_extension = _file.split(b".")[1]
            if file_extension == "c":
                c_file_count += 1
                # noinspection PyUnboundLocalVariable
                COMPILE = ("gcc %s%s -o %s%s.exe 2>/dev/null" %
                           (dir_location, _file, dir_location, _file))
                try:
                    subprocess.check_call(COMPILE, shell=True)
                    success_exe += 1
                except:
                    continue

        print("[+] Among %d C file[s], successfully compiled %d file[s]" %
              (c_file_count, success_exe))
        print("[+] Compiled file placed inside %s" % dir_location)
    else:
        print("[-] Exiting...")
        sys.exit(0)

# TODO!!! Make tar ball, too tired now
# print("[*] In order to transfer the script conveniently to target box")
# tar_answer = input("[*] Do you want to make a tar ball of the file? [y/n]")
# if tar_answer.lower() == "y":
#    TAR = 'tar -cvf %s.tar %s' % (dir_location, dir_location)
#    subprocess.call(TAR, shell=True)
