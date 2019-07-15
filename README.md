# Time-Series-Analysis

The thought process of the project is to build a trend recommendation engine which is independent of any domain that could browse the internet and retrieve the trends, currently and trends that are possibly futuristic

## Web Crawler

The first stop of the project is the web crawler. The web crawler is simply responsible for extracting data from the internet. The internet is huge. It is theortically impossible for us to send the crawler into the dark expecting it to bring back data. There has to be sources from which the Web Crawler and extract data from. For a small implementation, we can start sourcing the data from 3 different domains which predominantly takes up 70% of the internet. Social Media, articles and blogs. Whilst there is only a thin difference between articles and blogs, it brings a significant difference to the table when the recommendation is being considered. Articles are artifacts from expert personalities while the blogs are from general people who are self experts of the field. Being given a domain, the web crawler is responsbile for extracting the data from the 3 domains. The output of the crawler will be processed and submitted to the model which processes further.
