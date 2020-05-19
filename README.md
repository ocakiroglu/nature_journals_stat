# Nature Journals Stat
The project is created in order to access to a [Nature](https://www.nature.com/) article by a given article URL and print most cited 
* advisors
* journals
* or years

by user demand.

## Summary of the Project
[Nature](https://www.nature.com/) is a famous science journal and it consists of many subjournals and each of them is related to a subject such as photonic, environment and etc. Articles written by researchers are published separately in each sub journals as hard copy or digital in websites.

This project is created for digital version of Nature articles. Their common feature is that syntax in websites are same. Therefore, we can access to some of information related to the article by using the similarity. Unfortunately, all parts of articles are not accessable since most articles are not free. However, their reference list is open-access.

The aim is to use this similarity between sub journals and to determine most cited features in references.

**PS:** The script is command-line program and is written on Python3.

**PS:** Required Python Libraries are [urllib](https://docs.python.org/3/library/urllib.html) and [numpy](https://numpy.org/).

## How to Use
Simple command structure should be like that

`python3 nature_journals_stat.py [Article URL] [Feature] [Number]`

####Examples

Nature Article Url as a Sample: [https://www.nature.com/articles/natrevmats201733](https://www.nature.com/articles/natrevmats201733)

* Print 10 Most Cited Journals

`python3 nature_journals_stat.py https://www.nature.com/articles/natrevmats201733 Journal 10`

Output:

	Journal             :	 Number of Citation
	-------------------------------------------
	Nano Lett.          :	 	29
	Phys. Rev. B        :	 	27
	ACS Nano            :	 	23
	Phys. Rev. Lett.    :	 	14
	Nat. Nanotechnol.   :	 	11
	Science             :	 	10
	Adv. Mater.         :	 	8
	Nat. Mater.         :	 	8
	Nat. Phys.          :	 	6
	2D Mater.           :	 	5


* Print 7 Most Cited Advisors

`python3 nature_journals_stat.py https://www.nature.com/articles/natrevmats201733 Advisor 7`

Output:

	Advisor             :	 Number of Citation
	-------------------------------------------
	A Kis               :	 	8
	BI Yakobson         :	 	4
	J Pu                :	 	3
	TF Heinz            :	 	3
	W Wu                :	 	2
	J Shan              :	 	2
	S Najmaei           :	 	2


* Print 5 Most Cited Years

`python3 nature_journals_stat.py https://www.nature.com/articles/natrevmats201733 Year 5`

Output:

	Year                :	 Number of Citation
	-------------------------------------------
	2015                :	 	40
	2016                :	 	36
	2014                :	 	35
	2013                :	 	28
	2012                :	 	19


<br />

#### Arguments
Article URL: Any Desired Nature Article URL 

Feature: Journal or Year or Author

Number: Any Desired Number of Most Cited Feature

<br />

**PS:** If given number is larger than existed feature (such as author), max number of feature is set automically. 

<br />

## TO-DO LIST
* Error Handling
* Detect Cited Book and Remove Them to Count
* Detect Arxiv Paper and Add Them to Cound
* Import Text File Consisting of URL List and Print Most Cited for All
