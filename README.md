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



# **Authors**
Developed by Daramola Oluwasegun, Akomolafe Ayobami, Adedeji Roqeeb, and Agboeze Tochukwu using the LUCAS dataset as part of the AI4LS Challenge #1 and the GSMc dataset.


