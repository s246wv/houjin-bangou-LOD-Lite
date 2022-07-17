# 法人番号LOD-Lite

will be added later 

## Description

Unfortunately, the great successor, [日本の法人LDO](http://idea.linkdata.org/idea/idea1s1417i) was not reachable now. This repository provides the yet-another-LOD-version of the [Corporate Number](https://www.houjin-bangou.nta.go.jp/).  
This dataset ...

## Usage of python script

If you want to create the ttl file by yourself, please use the python script, houjinLOD.py.
1. Download the csv file from https://www.houjin-bangou.nta.go.jp/.  
2. Install the requirement packages.
3. Edit the line number 9 of houjinLOD.py to match the file name which you downloaded.
4. Run it!

*Maybe this script needs much memory because of creating quite straightforward. I appreciate if anyone improve the code more sophisticated.*

## Requirement
pandas  
rdflib  

## Acknowledgement
I appreciate the following works to create this dataset.

- [国税庁 法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/)
- [PURL service](https://purl.archive.org/) provided by an initiative of the [Internet Archive](http://archive.org/)

## License 
法人番号LOD-Lite is licensed under a [Creative Commons Attribution-4.0 International License.](https://creativecommons.org/licenses/by/4.0/) based on a work at https://www.houjin-bangou.nta.go.jp/riyokiyaku/