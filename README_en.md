# 法人番号LOD-Lite
## Description
The Corporate Numbers are the identifiers that represents companies and other organizations registered in Japan. National Tax Agency in Japan provides corporate information with the Corporate Numbers at Corporate Number Publication Site. Previously, Igata and Morikawa published "[日本の法人LOD](http://idea.linkdata.org/idea/idea1s1417i)" as a LOD version of the Corporate Numbers. The "日本の法人LOD" was well designed to organize the dataset using various standard schema. However, the dataset was not reachable now. Based on the background, I would like to use the Corporate Numbers information as a Linked Data. Therefor, I created this simple dataset. I understood the following shortages and I appreciate it if anyone improve this dataset.

## Known Shortages of the Dataset
1. **Lack of schema**  
   This dataset uses the original properties without any definitions. It does not provide any benefit from other ontologies and linked data.
2. **No linkage with other resources**  
   This dataset was created by only the Corporate Numbers. It does not provide any linkage with other resources. So, it may not be able to say "linked data" yet.
3. **Lack of maintainers**  
   I have no plan to maintain this dataset. I hope anyone maintains this dataset or publish yet-another better LOD version of the Corporate Numbers.  

## Usage of the Python Script

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