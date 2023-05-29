# 4chanScraper
4Chan simple python board scraper

## How to use?
First run 
```python
 python main.py
```
Then, to download all the images from the csv file, run this powershell script
```Powershell
Get-Content 4chan_image_urls.csv | Sort-Object -Unique | ForEach-Object { Invoke-WebRequest $_ -OutFile (Split-Path $_ -Leaf) } 
```
