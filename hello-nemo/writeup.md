# Hello Nemo

### Challenge

We just managed to intercept Cpt. Nemo of the Nautilus submarine. Something's fishy over here...
Download nemo.pcapng and start the investigation.

Flag format: DCTF{sha256}

### My solution

Scrolling through the pcap, we see commands that look like FTP commands. First a user tries to login, and we see he manages to login with `dctf : dctf` credentials. Then he lists all files, of current directory, cd into `files`, and lists files in there. We see a `flag.txt` file, but as the user does not try to read it we don't have any info about the content of this file...

A couple commands after, the user uploads a file named `flag.zip`. Is the flag in this file ? I extract it from the pcap, and try to open it. Aaaand... Fuck, it prompts for a password...

Let's find that password !

Scrolling and scrolling, we see a weird command : `cat dgyfogfoewyeowyefowouevftowyefg > password.txt`. This command is obviously broken as no file is named `dgyfogfoewyeowyefowouevftowyefg`. So maybe the password is the error message ? I try... No, it isn't. By chance, I try to enter `dgyfogfoewyeowyefowouevftowyefg` as password, as I guess this was the intention of the user, and indeed, the zip file unlocks and I have the flag !
