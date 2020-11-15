#!/bin/bash
for b in InRelease repomd.xml primary.xml.gz filelists.xml.gz ; do 
    for a in  $(grep $b /srv/install/proxy/*_url | sed s/_.*//) ; do 
	rm $a* 
    done
done
