# strabo-learning-ocr-transformation-hpc
This project is based on [Rashmina's project](https://github.com/spatial-computing/strabo-learning-ocr-transformation). However, Rashmina's project can not be run on HPC because of some limitations and the classifiers can not be trained parallelly which requires a lot of time to complete the training.

### CSV files
There are two csv files in this project.

* __label.csv__ is the original data used by Rashmina's project.
* __label3.csv__ is the data file without duplicated samples.

The file __label.csv__ is too large to upload to the github, you can generate it again on the server by running
> python Data.py

The model we trained in Spring 2016 is based on __label.csv__, but finding a way to train the model with __label3.csv__ should save a lot of time.

### Modified Python files

* __gbc.py__ the classifier is changed and it just trained one classifer for a given label now.
* __classify_gbc.py__ the function _sequence2_ should give the score of two aligned words.
* __generate_pbs.py__ generate the script used in the HPC.


