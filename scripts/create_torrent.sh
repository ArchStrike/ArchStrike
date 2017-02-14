#!/bin/bash
iso=$1
arch=$2

checksums(){
sha512sum $iso > sha512sum-${arch}.txt
sha512sum -c sha512sum-${arch}.txt
sha256sum $iso > sha256sum-${arch}.txt
sha256sum -c sha256sum-${arch}.txt
}

create_sigs(){
 gpg --default-key <keyid> --output ${iso}.sig -b ${iso}
 gpg --verify ${iso}.sig ${iso}
}



create_torrent(){
mktorrent -a udp://tracker.coppersurfer.tk:6969/announce,udp://tracker.ccc.de:80/announce,udp://tracker.publicbt.com:80,udp://tracker.istole.it:80,http://tracker.openbittorrent.com:80/announce,http://tracker.ipv6tracker.org:80/announce \
          -n "${iso}" -v \
          -o ${iso}.torrent \
          -c "The ArchStrike Project is an Arch Linux based Distro for security professionals and enthusiasts." \
          -w https://mirror.archstrike.org/os/$iso \
          -w https://uk.mirror.archstrike.org/os/$iso \
          -w https://jp.mirror.archstrike.org/os/$iso \
          -w http://archstrike.outerworld.org/os/$iso \
          -w https://mirror.wh1t3fox.net/archstrike/os/$iso \
          -w http://mirror.i3d.net/pub/archstrike/os/$iso \
          -w http://mirror.keystealth.org/archstrike/os/$iso \
          -w http://mirrorservice.org/sites/mirror.archstrike.org/os/$iso \
          -w http://mirror.jmu.edu/pub/archassault/os/$iso \
          ${iso}
}

main(){
 create_torrent
 checksums
 create_sigs
}

main
