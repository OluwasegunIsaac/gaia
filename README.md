# gaia - Geographic AI for Soil Assessment
This README file provides information about the packages and datasets used in the code provided.

Our cutting-edge AI-powered dashboard (gaia) leverages Artificial Intelligence / Machine Learning methods, advanced geographic visualization and analysis to provide accurate predictions and develop a deeper understanding of the role of the soil microbiome to contribute to soil health. We used the Land Use / Cover Area frame statistical Survey Soil (LUCAS Soil) dataset obtained from the Joint Research Centre European Soil Data Centre (ESDAC) in collaboration with the AI4LS Virtual hackathon series, to develop a multi-tiered dashboard that can predict and visualize soil microbial (bacterial and fungal) biodiversity, establish relationships between different soil condition predictors and features through statistical analytic approaches, and generate hypothesis about soil health condition drivers. We also incorporated the elaborate Global Soil Mycobiome consortium (GSMc) dataset, to boost the model prediction of soil fungal richness and biodiversity.

# App Link
Here is the link to the webapp deployed via Streamlit: https://gaia-app.streamlit.app/

![image](https://github.com/OluwasegunIsaac/gaia/assets/102333264/3d17a35e-b676-410c-8394-3187fc4b5894)


# Required Packages
The following packages are imported in the code:
- streamlit
- streamlit-option-menu
- pandas
- numpy
- scikit-learn==1.2.2
- joblib
- catboost
- plotly

# Datasets
The raw dataests used for this projects are:
- The Land Use / Cover Area frame statistical Survey Soil (LUCAS Soil) dataset which is a European Union effort to survey European topsoil characteristics and Microbiome sequence data from the LUCAS Soil Survey for prokaryotes, fungi, and microeukaryotes. Avalaible here: https://esdac.jrc.ec.europa.eu/projects/lucas
- The global soil fungal dataset of the Global Soil Mycobiome consortium (GSMc), which comprises 722,682 fungal operational taxonomic units (OTUs) from 3200 plots in 108 countries on all continents. The OTUs are taxonomically and functionally assigned to guilds and other functional groups. Available here: https://doi.plutof.ut.ee/doi/10.15156/BIO/2263453

# Microbiome Bioinformatics Analysis
## Steps to Run the Analysis
1. Set Up Qiime2 Environment
Set up your Qiime2 environment by following the instructions from Qiime2 Documentation
https://docs.qiime2.org/2023.9/install/

2. Create Directories for Analysis
Create two new directories: one for bacteria analysis and another for fungi analysis.

Bacteria Directory Contents:
	bacteria.pairedmanifest.sh
	bacteria_download_links.txt
	bacteria.analysis.sh

Fungi Directory Contents:
	fungi.pairedmanifest.sh
	fungi_download_links.txt
	fungi.analysis.sh

3. Organize Relevant Files
Move all relevant files to their respective directories. Ensure that reference files from the respective databases (SILVA 138 for bacteria and UNITE QIIME release version 9.0 for fungi) are saved in their respective folders.

4. Download Files
In each directory, use the following command to download the files specified in the _download_links.txt:

bash
Copy code
		wget  -i *download_links.txt

Check to ensure that all the necessary files have been successfully downloaded.

5. Create Manifest Files
Use the provided manifest.sh files to generate the manifest files required for Qiime2 import.

6. Run Analysis Scripts
Navigate to each directory and execute the analysis.sh files. Before running, review the content of these files to ensure that all necessary files are accounted for and modify the scripts as needed to suit your specific analysis requirements.


## Info

We used the files available from ENA because the AWS bucket will be shut down soon.
To get the AWS bucket links check the AWS_bucket_links.sh to see the download scripts

![newplot](https://github.com/OluwasegunIsaac/gaia/assets/102333264/fa3c3b51-94d3-4c21-91e4-ee72c389c89d)


# Land Use / Cover Area frame statistical Survey Soil (LUCAS Soil) Dataset
The Land Use / Cover Area frame statistical Survey Soil (LUCAS Soil) dataset is a European Union effort to survey European topsoil characteristics and Microbiome sequence data from the LUCAS Soil Survey for prokaryotes, fungi, and microeukaryotes.
![land_use2](https://github.com/OluwasegunIsaac/gaia/assets/102333264/151b98b6-f294-4307-8363-27b7cd319bbe)

## LUCAS Interactive Maps
The interactive maps for each datasets were toolarge for fast efficiency on the streamlit app, hence a demo for navigating it was inserted. To interact with the maps and sample points, the html files for the maps have been uploaded to this drive link: (https://drive.google.com/drive/folders/1Wh5JnYuZVs4gmfrxFYgMAmnb28v6EFVH?usp=drive_link)

# Global Soil Mycobiome consortium (GSMc) Dataset

The GSMc model is built using the global soil fungal dataset of the Global Soil Mycobiome consortium (GSMc), to boost further prediction of soil fungal biodiversity, biogeography and macroecology in soil samples. The dataset comprises 722,682 fungal operational taxonomic units (OTUs) from 3200 plots in 108 countries on all continents. The OTUs are taxonomically and functionally assigned to guilds and other functional groups. The GSMc dataset is available from https://doi.plutof.ut.ee/doi/10.15156/BIO/2263453.

Citation: Tedersoo, Leho (2021): The Global Soil Mycobiome consortium dataset for boosting fungal diversity research v2. University of Tartu. 10.15
156/BIO/2263453
![global_anim2](https://github.com/OluwasegunIsaac/gaia/assets/102333264/51c409c4-05c8-4bda-a1fc-1a5b72f6ed96)



# **Authors**
Developed by Daramola Oluwasegun, Akomolafe Ayobami, Adedeji Roqeeb, and Agboeze Tochukwu using the LUCAS dataset as part of the AI4LS Challenge #1 and the GSMc dataset.


