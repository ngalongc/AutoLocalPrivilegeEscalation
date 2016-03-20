# AutoLocalPrivilegeEscalation
An automated script that download potential exploit for linux kernel from exploitdb, and compile them automatically

First, it search for linux pirvilege escalation from the exploitdb in local directory by searchsploit.
Pass in the kernel version as first parameter, it lists potential exploit, and ask if you want to copy them from the local directory.
After that, it asks if you want to compile the downloaded C file.
Then, it will ask if you want to make a tar ball of the directory.
And it will show the summary of the downloaded files.
