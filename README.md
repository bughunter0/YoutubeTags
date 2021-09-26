# YoutubeTags
**YoutubeTags is a python third-party api wrapper to Extract Youtube Tags without Youtube API**, **Capable to extract Video and Channel Tags**

[![Downloads](https://static.pepy.tech/personalized-badge/youtubetags?period=total&units=abbreviation&left_color=grey&right_color=yellow&left_text=Total-Downloads)](https://pepy.tech/project/youtubetags)
[![CodeQL](https://github.com/bughunter0/YoutubeTags/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/bughunter0/YoutubeTags/actions/workflows/codeql-analysis.yml)
[![Supported Versions](https://img.shields.io/pypi/pyversions/Youtubetags.svg)](https://pypi.org/project/YoutubeTags)
![GitHub](https://img.shields.io/github/license/bughunter0/YoutubeTags)
![PyPI](https://img.shields.io/pypi/v/youtubetags)
[![Documentation Status](https://readthedocs.org/projects/youtubetags/badge/?version=latest)](https://youtubetags.readthedocs.io/en/latest/?badge=latest)
![PyPI - Downloads](https://img.shields.io/pypi/dm/YoutubeTags)
[![Downloads](https://static.pepy.tech/personalized-badge/youtubetags?period=week&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads/Week)](https://pepy.tech/project/youtubetags)
[![Upload to PIP](https://github.com/bughunter0/YoutubeTags/actions/workflows/Pypi-uploads.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/bughunter0/YoutubeTags/actions/workflows/Pypi-uploads.yml)
![PyPI - Format](https://img.shields.io/pypi/format/YoutubeTags)


# Installation

```
pip install YoutubeTags
```

# Video Tags

## How to Use It

```python
import YoutubeTags

link = "Add Your Youtube Link Here" # Use https / http Links
variable_name = YoutubeTags.videotags(link)
print(variable_name)
```

> **_NOTE:_** ONLY SUPPORTS HTTP(S) , use HTTP(S) links to get the results 

## Example 1

```python
import YoutubeTags

findtags = YoutubeTags.videotags("https://www.youtube.com/watch?v=RTbrXiIzUt4") # Mkbhd's Video
print(findtags)
```

### Output of Example 1

```
Right To Repair, right to repair, MKBHD, right to repair movement, Apple, Apple vs, 
repairing iPhone, iPhone 12, Tesla right to repair, Apple right to repair
```

## Example 2

```python
import YoutubeTags

tags = YoutubeTags.videotags("https://www.youtube.com/watch?v=Kbe3FKeCd1A") # Karikku star Episode
print(tags)
```

### Output of Example 2

```
karikku, malayalam, funny, comedy, webseries, lolan,
george, karikk, karikke, film, trending, sketch, vine, flowerstv
```

## Example 3

```python
import YoutubeTags

gettag = YoutubeTags.videotags("https://www.youtube.com/watch?v=nvjILgpf6tc") # Video From Technical Guruji
print(gettag)
```

### Output of Example 3

```
iPhone 14, iPhone 14 Unboxing, iPhone 14 exclusive 1st look, iPhone 14 first look,
iPhone 14 no notch, iPhone 14 punch hole camera, iPhone 14 titanium sides, iPhone 14 look, 
iPhone 14 leaks, iPhone 14 design, iPhone 14 india, iPhone 14 launch date, iPhone 14 no camera bump,
iPhone 14 features, iPhone 14 price, iPhone 14 vs iPhone 13, iPhone 14 launch event, iPhone 14 india 1st look, 
iPhone 14 first look in hindi, Technical Guruji, Technicalguruji, Gaurav Chaudhary, 13
```

## Example 4 (If Video Has no tags)

```python
import YoutubeTags

tag = YoutubeTags.videotags("https://www.youtube.com/watch?v=Mlk888FiI8A") # Google Keynote video 2021 
if tag is None:
   print ("No Tags Found")
else:
   print(tag)
```

### Output of Example 4

```
No Tags Found
```

# Channel Tags

## How to Use It

```python
import YoutubeTags

link = "Add Your Channel Link Here" # Use https / http Links
variable_name = YoutubeTags.channeltags(link)
print(variable_name)
```

> **_NOTE:_** ONLY SUPPORTS HTTP(S) , use HTTP(S) links to get the results 

## Example 1
```python
import YoutubeTags

findtags = YoutubeTags.channeltags("https://youtube.com/c/mkbhd") # Mkbhd's channel Link
print(findtags)
```
### Output of Example 1

```
 MKBHD, MarquesBrownlee, Marques, Brownlee 
```

## Example 2

```python
import YoutubeTags

tags = YoutubeTags.channeltags("https://youtube.com/c/Karikku_Fresh") # Karikku channel Link
print(tags)
```
### Output of Example 2

```
 karikku, media, digital, malayalam 
```
## Example 3
```python
import YoutubeTags

gettag = YoutubeTags.channeltags("https://youtube.com/c/TechnicalGuruji") # Technical Guruji channel Link
print(gettag)
```

### Output of Example 3

```
 Hindi Technology, Technology in Hindi, Hindi Tech Guru, Technical Guruji, Hindi Tech Tips, Tech Reviews, Mobile Tips and Tricks, Technology Explained,
 Hindi Tech, Hindi Tech Reviews, Tech Hindi, hindi, Technology, Mobile, tech, Reviews, TechnicalGuruji, Gaurav Chaudhary, Smartphones, Mobile Phones,
 Tech, latest Tech,Cool Technology, Tech News, Latest Tech News 
```

## Example 4

```python
import YoutubeTags
from YoutubeTags import channeltags
tag = channeltags("https://youtube.com/user/PewDiePie") # PewDiePie channel Link
print(tag)
```

### Output of Example 4

```
  pewdiepie, pewds, gaming, felix arvid ulf, felix, kjellberg 
```

# License

<b>© 2021 Nuhman Pk, Licensed under [MIT License](/LICENSE)</b>

## Github

Follow me on [Github](https://www.github.com/bughunter0) and if you find this [library](https://github.com/bughunter0/YoutubeTags) useful don't forget to add Your star

## Sponsor this project
[ko-fi](https://ko-fi.com/nuhmanpk)<br>
[paypal](https://www.paypal.me/nuhmanpk)<br>
[Buy me a Coffee](https://www.buymeacoffee.com/nuhmanpk)
