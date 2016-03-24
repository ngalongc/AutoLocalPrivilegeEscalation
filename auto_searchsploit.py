#! /usr/bin/env python
import subprocess
import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('kernel_version', metavar='kernel_version', type=str,
                           help='Kernel Version')

args = parser.parse_args()
kern_ver = args.kernel_version

# You can tellThis search is very specific to Linux Local Privelege Escalation
SEARCH = "searchsploit linux %s | grep local | grep -i privilege" % kern_ver
try:
    search_results = subprocess.check_output(SEARCH, shell=True)
    file_list = []
    base_dir = "/usr/share/exploitdb/platforms/linux/local"
    dir_location = "%s/linux_%s/" % (os.environ['PWD'],kern_ver)
    c_found = False

    print "[*]Potential Exploit :"

    print search_results

    search_results = search_results.strip()
    search_results = search_results.split('\n')

    # try to copy to local directory first
    for result in search_results:
        result = result.split('/')
        file_name = result[-1]
        file_list.append(file_name)
    print "[*] File destination directory name: %s/linux_%s" % (os.environ['PWD'], kern_ver)
    download_ans = raw_input("[*] Do you want to download exploit file to directory described above? [y/n]")
    if download_ans == 'y' or download_ans == 'Y':
        new_dir = "mkdir %s" % (dir_location)
        # Make dir if not exist
        if not (os.path.isdir(dir_location)):
            subprocess.call(new_dir, shell=True)
        for _file in file_list:
            DOWNLOAD = "cp %s/%s %s" % (base_dir, _file, dir_location)
            subprocess.call(DOWNLOAD, shell=True)
        print "[+] All file downloaded in %s" % dir_location
    else:
        print "[-] Exiting..."
        sys.exit(0)

    # Now try to compile them if it is C
    for _file in file_list:
        file_extension = _file.split('.')[1]
        if file_extension == 'c' or file_extension == "C":
            c_found = True
            break

    if c_found:
        print "[*] C script found"
        print "[*] Compile format: gcc C_SCRIPT -o C_SCRIPT.exe"
        compile_ans = raw_input("[*] Do you want to compile the downloaded C script?(No Gurantee Success) [y/n]")
        if compile_ans == 'y' or compile_ans == 'Y':
            success_exe = 0
            c_file_count = 0
            for _file in file_list:
                file_extension = _file.split('.')[1]
                if file_extension == "c":
                    c_file_count += 1
                    COMPILE = "gcc %s%s -o %s%s.exe 2>/dev/null" % (dir_location,_file,dir_location,_file)
                    try:
                        subprocess.check_call(COMPILE, shell=True)
                        success_exe += 1
                    except:
                        continue

            print "[+] Among %d C file[s], successfully compiled %d file[s]" % (c_file_count, success_exe)
            print "[+] Compiled file placed inside %s" % dir_location
        else:
            print "[-] Exiting..."
            sys.exit(0)

    #TODO!!! Make tar ball, too tired now
    #print "[*] In order to transfer the script conviniently to target box"
    #tar_answer = raw_input("[*] Do you want to make a tar ball of the file? [y/n]")
    #if tar_answer == 'y' or tar_answer == "Y":
    #    TAR = 'tar -cvf %s.tar %s' % (dir_location, dir_location)
    #    subprocess.call(TAR, shell=True)

except subprocess.CalledProcessError as grepexc:
    print "[-] No potential exploit found. Aborting..."

