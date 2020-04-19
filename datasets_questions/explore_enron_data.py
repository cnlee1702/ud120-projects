#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

"""
    Credit to monkshow92 https://github.com/udacity/ud120-projects/issues/46
"""

original = "C:/Users/nal17/Documents/ud120-projects/final_project/final_project_dataset.pkl"
destination = "C:/Users/nal17/Documents/ud120-projects/final_project/final_project_dataset_final.pkl"

content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

enron_data = pickle.load(open('C:/Users/nal17/Documents/ud120-projects/final_project/final_project_dataset_final.pkl', "rb"))
