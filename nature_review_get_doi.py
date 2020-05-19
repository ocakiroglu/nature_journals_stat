import urllib.request
import sys

# url_link1 = "https://www.nature.com/articles/natrevmats201733#Bib1"
# url_link2 = "https://www.nature.com/articles/360444a0#Bib1"
url_link = str(sys.argv[1])
req = urllib.request.Request(url_link)  # requesting to access to the url
with urllib.request.urlopen(req) as f:
    url_data = f.read().decode()

starter = "<meta name=\"citation_reference\""
tot_ref_num = url_data.count(starter)
doi_store_list = []
each_ref_length = 0
for i in range(tot_ref_num):
    index_start = url_data[each_ref_length:].find(starter)
    index_end = url_data[each_ref_length + index_start:].find("/>")
    each_ref = url_data[each_ref_length + index_start:(each_ref_length + index_start + index_end + 2)]
    each_ref_lst = each_ref.strip().split(";")
    for j in each_ref_lst:
        if j.find("citation_doi=") != -1:
            doi = j.strip().replace("citation_doi=", "")
        if j.find("citation_id=") != -1:
            ref_num = j.strip().replace("citation_id=CR", "").replace("\"/>", "")
    each_ref_length = each_ref_length + index_start + index_end + 2
    doi_store_list.append([int(ref_num), doi])

with open(str(sys.argv[2]), 'w') as f:
    for i in range(tot_ref_num):
        f.write("[{}] doi: {}\n".format(doi_store_list[i][0], doi_store_list[i][1]))
