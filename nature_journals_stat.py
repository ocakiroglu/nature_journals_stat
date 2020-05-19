import urllib.request
from urllib.error import HTTPError
import numpy as np
import sys


def get_data_from_url(url_link):
    """Method takes a URL, access to it and get data inside it.
    Input:: String (Given URL by a User)
    Return:: String"""

    # Get Article URL Given by User, Connect to the URL and Decode What We Get
    req = urllib.request.Request(url_link)  # requesting to access to the url
    try:
        with urllib.request.urlopen(req) as f:
            url_data = f.read().decode()
    # Check Possible Errors, Give a Message and Stop the App.
    except HTTPError as e:
        if e.code == 404:
            print("Error 404: Page not Found.")
            quit()
        else:
            print("There's something wrong in accessing to URL.")
            quit()
    return url_data


def urldata_to_numpyarray(url_data):
    """Method takes a decoded data and get Advisors, Journals, Years and Ref IDs.
    Input:: String (Data in URL)
    Return:: Numpy Array (N,4)"""

    # Each Citation Starts with Such A Starter in Nature Article Website
    # Determine Where First Citation Starts
    starter = "<meta name=\"citation_reference\""
    # Count How Many Citation Exists in Website to Stop Searching Starter More After Last Ref.
    tot_ref_num = url_data.count(starter)
    store_list = np.array([])
    each_ref_length = 0
    for i in range(tot_ref_num):
        # Determine Beginning of Each Ref Starter Index in the String
        index_start = url_data[each_ref_length:].find(starter)
        # Determine End Index of Each Ref in the String
        index_end = url_data[each_ref_length + index_start:].find("/>")
        # Get Each Ref by Using Beginning of Starter and End Index
        each_ref = url_data[each_ref_length + index_start:(each_ref_length + index_start + index_end + 2)]
        # Split Ref as String to A List by A Separator
        each_ref_lst = each_ref.strip().split(";")
        for j in each_ref_lst:
            if j.find("citation_author=") != -1:  # Go to the Location of Authors Name
                authors = j.strip().replace("citation_author=", "")  # Get Authors Name
                advisor = authors.split(",")[-1]  # Get Last Author As An Advisor
            if j.find("citation_journal_title") != -1:  # Go to the Location of Journal
                # Get Journal Name
                journal = j.strip().replace("<meta name=\"citation_reference\" content=\"citation_journal_title=", "")
            if j.find("citation_publication_date") != -1:  # Go to the Location of Publication Year
                date = j.strip().replace("citation_publication_date=", "")  # Get Publication Year
            if j.find("citation_id=") != -1:  # Go to the Location of Ref ID
                ref_num = j.strip().replace("citation_id=CR", "").replace("\"/>", "")
        # Go to Next Ref Location by Using Length of Struggled One
        each_ref_length = each_ref_length + index_start + index_end + 2
        # Store Each Data in a Numpy Array
        store_list = np.append(store_list, [advisor, journal, date, ref_num])
        # Reshape Array and Make it Array as (N, 4)
        store_list = np.reshape(store_list, (int(len(store_list) / 4), 4))
    return store_list


def count_element_in_array(data_list, feature):
    """Method counts existed elements in a column determined by desired feature.
    Then return elements as much as desired number.
    Input:: Ref List, Feature
    Input Type:: Numpy Array(N,4), String
    Return:: Numpy Array, Numpy Array"""

    feature_lst = ["Advisor", "Journal", "Year"]
    index = feature_lst.index(feature)  # Determine What User Want as Feature
    unique, counts = np.unique(data_list[:, index], return_counts=True)  # Counts Features
    count_sort_ind = np.argsort(-counts)  # Determine Index of Counted Feature to ReOrder
    return unique[count_sort_ind], counts[count_sort_ind]


def print_result(sorted_feature, sorted_count, number=5):
    """Print Results in An Order
    Input:: Sorted Feature List, Sorted Count List, Desired Number of Lines in Print
    Input Type:: Numpy Array, Numpy Array, Integer"""

    # If given number is bigger than sorted list
    if number > len(sorted_feature):
        number = len(sorted_feature)

    print("\t{:20}:\t {}".format(str(sys.argv[2]), "Number of Citation"))
    print("\t"+"-"*43)
    for i in range(number):
        print("\t{:20}:\t \t{}".format(sorted_feature[i].strip(), sorted_count[i]))


print("Connection to URL is waiting ....")
data_in_url = get_data_from_url(str(sys.argv[1]))  # Get Data from URL
print("Connection is Successful and Data is Imported.\n")
feature_list = urldata_to_numpyarray(data_in_url)  # Get Ref Data as List
sorted_f, sorted_c = count_element_in_array(feature_list, str(sys.argv[2]))  # Count and Sort by Feature
print_result(sorted_f, sorted_c, int(sys.argv[3]))  # Print Desired Result by Desired Amount
