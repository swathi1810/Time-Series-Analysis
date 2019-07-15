# Time-Series-Analysis

The thought process of the project is to build a trend recommendation engine which is independent of any domain that could browse the internet and retrieve the trends, currently and trends that are possibly futuristic

## Web Crawler

The first stop of the project is the web crawler. The web crawler is simply responsible for extracting data from the internet. The internet is huge. It is theortically impossible for us to send the crawler into the dark expecting it to bring back data. There has to be sources from which the Web Crawler and extract data from. For a small implementation, we can start sourcing the data from 3 different domains which predominantly takes up 70% of the internet. Social Media, articles and blogs. Whilst there is only a thin difference between articles and blogs, it brings a significant difference to the table when the recommendation is being considered. Articles are artifacts from expert personalities while the blogs are from general people who are self experts of the field. Being given a domain, the web crawler is responsbile for extracting the data from the 3 domains. The output of the crawler will be processed and submitted to the model which processes further.

## Machine Learning Model

The Machine Learning Model is the heart of the project. The crawler retreives all the data from the interent and produces it to the model. The model is responsible for understanding the data and predict the current and the future trends. The Model has to understand the context and the semantics of the data and graph the trends. 

## Architecture

It is very important to understand that the project is in a very early stage and there is no vital importance to the UI or how the output is produced. The output of the experiment is a minimal viable product.

## OUTPUT

The expected output from the project is to take a particular domain and see the model predicts the trends. There is a greator risk of the project to be non viable but it is completely fine.
