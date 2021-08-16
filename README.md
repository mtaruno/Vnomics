# Vnomics

This project represents the final capstone project for the Data Science bachelors program at the University of Rochester that we made for the startup [Vnomics](https://www.vnomicscorp.com). Check out the final presentation PDF file named `Capstone Final Presentation` or `Vnomics 1 Final Report` for motivations and intuitive visuals for understanding this project.

### Steps to run the files:
- to reproduce the model performance: run all the code in Comprehensive_Model_Testing.ipynb
- We wrote the code in databricks. If databricks is not available to you, please ignore the second cell. Replace "tsf_comp = pd.read_csv("/dbfs/FileStore/shared_uploads/mtaruno@u.rochester.edu/X_tsf_window_20_comprehensive_label.csv")" with "tsf_comp = pd.read_csv("/YourDirectory..../X_tsf_window_20_comprehensive_label.csv")"
- please ignore cells relevant to hyperopt, if MLOps is not in your library (usually they will be the first five cells in each autoencoder section)
	For example, the run_dense(n) function requires hyperopt to run. These functions are for hyperparameter tuning. We have already saved the output from MLflow. Please feel free to just run the training. 
- The data files involved are “vehicle_list.csv” and “X_tsf_window_20_comprehensive_label.csv”. 


### Additional information: 

For Feature Engineering: 
- We did feature engineering in order to choose the best features to be fed to the autoencoder. Therefore, we first found a list of relevant features to choose through feature selection process(random forest, SMOTE, PCA, TSFresh). Then, we chose these features from TSFresh and obtained the training data. The file "X_tsf_window_20_comprehensive_label.csv" is the example final output. 

The exact procedures to select the features and obtain the results are very sophisticated and takes a very long time to run. If you are interested in how we select the features and generate the data, please feel free to take a look into "Random_Forest_Dan_updated.ipynb", "matt_feature_selection.ipynb", "PCA_Daniel", and "matt_TSFresh.ipynb". 

### Note on Environment

Note that most of these notebooks were managed and containerized on a Databricks cluster and some commands may be specific to that environment such as display() and the use of ML Ops stack. Also, MLflow is used to hypertune the models using the interface and registry.

Setting up the environment will involve the packages in the `requirements.txt`. Additionally, get Tensorflow 2.4.1, HyperOpt version 0.2.5.db1, and MLFlow version 1.15.0. 

### Our Recommendation

For ease of access, since it is hard to reproduce our work for some parts without a Spark cluster, we recommend that you take a look at our HTML output for grading purposes in combination with some of our submitted notebook files (which serves more as a peripheral support for the main code we have made in the HTML outputs). Our main code we made sure to make into an HTML for your readability!

Note also that some notebooks you may have noticed access functions from `utilities.py`, `line.py`, and `tsf_pipeline.py`. These are modules we made to keep the code manageable. I have included HTML output to those too so you can see what functions were involved there, do check those out!

## Notebook Descriptions:

The most important notebooks are in the HTML files.

Beyond that:

Below are all the files relevant to feature engineering: 
matt_feature_selection.ipynb
matt_TSFresh.ipynb
Random_Forest_Dan_updated.ipynb
Feature_Engineering.ipynb
PCA_Daniel.ipynb
matt_label_attachment.ipynb


All relevant files for Autoencoder and hyperparameter tuning
Complete_Autoencoder_Pipeline.ipynb
Autoencoder_newest.ipynb
Comprehensive_Model_Testing.ipynb
Synthetic_50_model.ipynb
Hypertune_MLOps.ipynb


For EDA:
We added a subdirectory in notebooks/EDA where you can find the notebooks we utilized for EDA. 

all relevant EDA files:
EDA_London.ipynb
matt_EDA_Wrangling.ipynb

