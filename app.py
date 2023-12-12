import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib
import pickle
import base64
import plotly.express as px
from streamlit_option_menu import option_menu
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import warnings
warnings.filterwarnings("ignore")


man_prediction_=None
env_prediction=None
rich=None
abund=None
pred_richness_= None
pred_abundance_ =None
Unassigned =None
Saprotroph_Symbiotroph =None
Saprotroph = None
Pathotroph_Saprotroph_Symbiotroph =None
Symbiotroph =None
Pathotroph_Symbiotroph =None
Pathotroph = None
Pathotroph_Saprotroph=None


country=['Austria','Portugal', 'Spain', 'Belgium', 'Bulgaria', \
       'Cyprus', 'Czech Republic', 'Germany', 'Denmark', 'Estonia',\
       'Greece', 'France', 'United Kingdom', 'Finland', 'Sweden',\
       'Slovenia', 'Italy', 'Croatia', 'Hungary', 'Ireland', 'Lithuania',\
       'Luxembourg', 'Latvia', 'Malta', 'Netherlands', 'Poland',\
       'Romania', 'Slovakia']
Land_cover=['Woodland', 'Cropland', 'Grassland', 'Artificial land', \
       'Shrubland', 'Bareland', 'Wetlands', 'Water'] 
Land_description=['Spruce dominated coniferous woodland', 'Barley', 'Common wheat',\
       'Sugar beet', 'Maize', 'Grassland without tree/shrub cover', \
       'Broadleaved woodland', 'Soya', 'Spruce dominated mixed woodland',\
       'Non built-up area features', 'Temporary grassland', \
       'Other mixed woodland', 'Triticale', 'Rye', \
       'Spontaneously re-vegetated surfaces', 'Other coniferous woodland', \
       'Shrubland without tree cover', 'Other fruit trees and berries', \
       'Non built-up linear features', \
       'Grassland with sparse tree/shrub cover', 'Apple fruit', \
       'Pine dominated mixed woodland', 'Other bare soil', 'Olive groves', \
       'Pine dominated coniferous woodland', \
       'Shrubland with sparse tree cover', 'Potatoes',\
       'Other artificial areas', 'Inland marshes', 'Nuts trees', \
       'Pear fruit', 'Other Leguminous  and mixtures for fodder' \
       'Other root crops', 'Other fibre and oleaginous crops', \
       'Other fresh vegetables', 'Durum wheat', 'Oats', \
       'Rape and turnip rape', 'Sunflower', 'Vineyards', 'Dry pulses', \
       'Permanent industrial crops', 'Lucerne', 'Rice', 'Cherry fruit', \
       'Other non-permanent industrial crops', 'Tobacco', \
       'Mix of cereals', 'Oranges', 'Tomatoes', 'Other cereals', \
       'Clovers', 'Nurseries', 'Peatbogs', 'Arable land (only PI)', \
       'Sand', 'Cotton', 'Inland fresh running water', \
       'Other citrus fruit', 'Floriculture and ornamental plants', \
       'Salines', 'Strawberries', 'Inland salty water bodies', \
       'Rocks and stones', 'Lichens and Moss']
depth=['0-20 cm', '0-10 cm', '10-20 cm', '20-30 cm']

bs=[' temperate coniferous forest biome', \
       ' tropical broadleaf forest biome', ' montane shrubland biome',\
       ' temperate broadleaf forest biome', ' temperate shrubland biome',\
       ' mediterranean forest biome',\
       ' subtropical broadleaf forest biome', ' tropical woodland biome',\
       ' woodland: temperate woodland biome', ' village biome',\
       ' subpolar coniferous forest biome',\
       ' flooded grassland biome', ' urban biome',\
       ' montane grassland biome', ' cropland biome',\
       ' tropical coniferous forest biome', ' temperate grassland biome',\
       ' rangeland biome', ' tropical desert biome',\
       ' xeric shrubland biome', ' temperate desert biome',\
       ' subtropical coniferous forest biome',\
       ' subtropical woodland biome', ' savanna biome',\
       ' tropical grassland biome', ' tropical shrubland biome',\
       ' subtropical grassland biome', ' subtropical shrubland biome',\
       ' subtropical desert biome', ' polar desert biome',\
       ' temperate woodland biome', ' montane desert biome']

def  main():
    #Wide format
    st.set_page_config(layout="wide")



    # Option menu in the top bar


    testing = option_menu(
        menu_title=None,
        options=["Home", "Data Summary", "Visualization" , "Analysis" , "LUCAS Model", "GSMc Model" ],
        icons=["house","grid-1x2-fill", "globe-central-south-asia" ,"gear","calculator","calculator"],
        orientation='horizontal',
        styles={
            "container": {"padding": "0!important", "background-color": "#63A86D"},
            "icon": {"color": "#01252C", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#63A86D",
            },
            "nav-link-selected": {"background-color": "#01252C"},
        },
    )



    #Home message
    if testing == "Home":
        
        st.image("images/cover.png")
        st.markdown('''[![Github Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/OluwasegunIsaac/gaia)''')
        st.markdown("<br>",unsafe_allow_html=True)    
        
        with st.sidebar:
            st.image("images/cover.png")
            st.info("""Welcome to the Geographic AI for Soil Assessment **(gaia)** interface, your ultimate companion in Predicting and visualizing soil microbial biodiversity.""") 
            st.info("""Our cutting-edge AI-powered dashboard **(gaia)** leverages Artificial Intelligence / Machine Learning methods, advanced geographic visualization and analysis to provide accurate predictions and develop a deeper understanding of the role of the soil microbiome to contribute to soil health. We used the Land Use / Cover Area frame statistical Survey Soil (LUCAS Soil) dataset obtained from the Joint Research Centre European Soil Data Centre (ESDAC) in collaboration with the AI4LS Virtual hackathon series, to develop a multi-tiered dashboard that can predict and visualize soil microbial (bacterial and fungal) biodiversity, establish relationships between different soil condition predictors and features through statistical analytic approaches, and generate hypothesis about soil health condition drivers. We also incorporated the elaborate Global Soil Mycobiome consortium (GSMc) dataset, to boost the model prediction of soil fungal richness and biodiversity.""")
            st.info("""Developed by **Daramola Oluwasegun, Akomolafe Ayobami, Adedeji Roqeeb,** and **Agboeze Tochukwu** using the LUCAS dataset as part of the [AI4LS Challenge #1](https://ai4lifesciences.com/) and the GSMc dataset.""")
            st.markdown('''[![Github Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/OluwasegunIsaac/gaia)''')
            st.markdown("<br>",unsafe_allow_html=True)

        image_path = 'images/heatmap.png'
        st.image(image_path, caption='Heatmap of sample collection points across Europe', use_column_width=True)


       
    
    if testing == "Data Summary":
        st.title('LUCAS Microbiome Exploratory Analysis')

        import plotly.express as px

        bacteria = pd.read_csv('taxonomy/bac_tax_div.csv')
        fungi = pd.read_csv('taxonomy/fun_tax_div.csv')

        st.markdown('<h1 style="font-size:24px;">Taxonomy Diversity of the 2018 LUCAS Bacterial sequenced samples</h1>', unsafe_allow_html=True)
        bacteria['Normalize_totalK'] = bacteria.groupby('Phylum')['totalK'].transform(lambda x: x / x.sum())

        fig = px.treemap(bacteria, path=['Phylum', 'Class', 'Order'], values='Normalize_totalK')
        st.plotly_chart(fig, use_container_width=True)

        top5_Phyla = 5
        top_Phyla = bacteria.sort_values('totalK', ascending=False).head(top5_Phyla)

        fig = px.treemap(top_Phyla, path=['Phylum'], values='totalK',title=f'Top 5 Bacteria Phyla by Diversity')
        st.plotly_chart(fig, use_container_width=True)


        text = '''
        ---
        '''

        st.markdown(text)

        
        st.markdown('<h1 style="font-size:24px;">Taxonomy Diversity of the 2018 LUCAS Fungal sequenced samples </h1>', unsafe_allow_html=True)
        fungi['Normalize_totalK'] = fungi.groupby('Phylum')['totalK'].transform(lambda x: x / x.sum())

        fig = px.treemap(fungi, path=['Phylum', 'Class', 'Order'], values='Normalize_totalK')
        st.plotly_chart(fig, use_container_width=True)

        top5_Phyla = 5
        top_Phyla = fungi.sort_values('totalK', ascending=False).head(top5_Phyla)

        fig = px.treemap(top_Phyla, path=['Phylum'], values='totalK',title=f'Top 2 Fungi Phyla by Diversity')
        st.plotly_chart(fig, use_container_width=True)




    if testing == "Visualization":
        st.title('Geographic Distribution of the LUCAS Dataset')

        #HTML Embedding Format too large for fast Streamlit interaction
        #st.header('Geographical points of the LUCAS 2018 data and its features')
        #HtmlFile = open("map_2018.html", 'r', encoding='utf-8')
        #source_code = HtmlFile.read() 
        #print(source_code)
        #components.html(source_code)

        st.markdown('<h1 style="font-size:24px;">Geographical points of the LUCAS 2018 data and its features</h1>', unsafe_allow_html=True)
        video_file = open('video/map.webm', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

        st.write(""" Link to the Interactive maps are embedded below:
        [LUCAS Interactive Maps (2009, 2015, 2018)](https://drive.google.com/drive/folders/1Wh5JnYuZVs4gmfrxFYgMAmnb28v6EFVH?usp=drive_link)
        """)

        text = '''
        ---
        '''

        st.markdown(text)
        
        st.markdown('<h1 style="font-size:24px;">Physiochemical properties per point for each Land Use category of the LUCAS 2018 data</h1>', unsafe_allow_html=True)
        file_ = open("gifs/land_use2.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="gif">',
        unsafe_allow_html=True, 
        )

        text = '''
        ---
        '''

        st.markdown(text)

        st.markdown('<h1 style="font-size:24px;">Physiochemical properties by Land Use of the LUCAS 2015 and 2018 data</h1>', unsafe_allow_html=True)
        file_ = open("gifs/land_use1.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="gif">',
        unsafe_allow_html=True, 
        )

        text = '''
        ---
        '''
        st.markdown(text)

        st.markdown('<h1 style="font-size:24px;">Physiochemical properties by Land Management of the LUCAS 2015 and 2018 data</h1>', unsafe_allow_html=True)
        file_ = open("gifs/land_man1.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="gif">',
        unsafe_allow_html=True, 
        )

        text = '''
        ---
        '''

        st.markdown(text)


        st.title('Geographic Distribution of the GSMc Dataset')
     
        file_ = open("gifs/global_anim1.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="gif">',
        unsafe_allow_html=True, 
        )


    if testing == "Analysis":
        st.title(' Addressed Analysis')

        st.header('Point 1: How incorporating microbial diversity improve predictions of soil carbon storage', divider='rainbow')

        data = {
        'Model Name': ['Random Boost', 'Gradient Boost', 'Xg boost', 'Cat boost', 'Decision tree'],
        'With Microbial diversity features': [7.118499999999996, 7.118499999999996, 8.114407950860482, 7.2704484609951745, 10.058333333333334],
        'Without Microbial Diversity features': [6.89975925925926, 6.89975925925926, 8.520341770737259, 7.787718401772183, 10.164814814814816],
        }
        df = pd.DataFrame(data)

        st.markdown('<h1 style="font-size:24px;">Comparison of MAE scores of models predicting Soil Carbon Storage</h1>', unsafe_allow_html=True)
        st.table(df)
        st.write("""
       **INFERENCE:** The impact of incorporating microbial diversity features varies among the models. For Random Boost, Gradient Boost, and Decision Tree, there is no clear improvement with microbial diversity features, this is further explained with the feature importance image, that shows that the main parameter in the prediction of soil carbon storage is the Nitrogen content. However, for Xg Boost and Cat Boost, there is a slight degradation in performance when including microbial diversity features.
       """)



        image_path = 'images/feature_imp_graph.png'
        st.image(image_path, caption='Comparison of the Feature Importance scores of both models', use_column_width=True)

        text = '''
        ---
        '''
        st.markdown(text)

        
        st.header('Point 2: Determine the relationship between physical, chemical, and biological features and generate hypotheses about co-linear features', divider='rainbow')

        col1, col2 = st.columns(2)

        image_path = 'images/correlation matrix.png'
        image_path2 = 'images/scatter_matrix.png'
        col1.image(image_path, caption='Correlation matrix', use_column_width=True)
        col2.image(image_path2, caption='Scatter plot matrix', use_column_width=True)

        st.markdown('<h1 style="font-size:24px;">Relationships between physical, chemical, and biological features</h1>', unsafe_allow_html=True)
        st.write("""
       **Chemical Variables:** The very strong positive correlation between pH_H2O and pH_CaCl2 suggests that these measures of soil pH are nearly equivalent. Researchers may consider using only one of these measures to avoid redundancy in their analyses.
       There are strong negative correlations between BD 0-10 and OC, N, and pH_H2O, suggesting potential collinearity.

       **Physical Variables:** BD 0-20 is strongly correlated with BD 0-10 and BD 10-20, indicating consistency in bulk density measurements across different layers. This could indicate a stable pattern of soil compaction or texture throughout the soil profile.

       **Biological Variables:** The strong positive correlation between fungal abundance and OTU counts (0.75) indicates a consistent relationship between the overall abundance of fungi and the number of unique fungal species.
        """)

        st.markdown('<h1 style="font-size:24px;">Hypotheses about co-linear features</h1>', unsafe_allow_html=True)
        st.write("""
       - The strong correlations suggest that certain variables indicate potential collinearity and multicollinearity.
       - The negative correlations between Bulk Density and Organic Carbon, Nitrogen, and pH_H2O highlight potential soil quality issues, as higher bulk density is associated with lower organic carbon, nitrogen content, and lower soil pH, which could have implications for nutrient availability.
       - Topological influences on soil structure can be responsible for the negative correlation between Bulk density and Elevation, hence, tendency for lower bulk density at higher elevations. 
        """)
        




    if testing == "LUCAS Model":
        st.subheader('Soil Microbial  (Fungi & Bacteria) Richness and Abundance Predictor')
        html_temp = """
        <div style="background-color:#01252C;padding:3px">
        <h2 style="color:white;text-align:center;"> Please input your predictor variables below  </h2>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)

        with st.form("my_form"):
            st.markdown('<h2 style="font-size:20px;">NB: Input zero (0) for parameters without values</h1>', unsafe_allow_html=True)            
            Country=st.selectbox('Country', country)
            Phosphorus_Content=st.number_input('Phosphorus Content (mg/kg)', min_value=0.0, step=0.1, value=20.0)
            Nitrogen_Content=st.number_input('Nitrogen Content (g/kg)', min_value=0.0, step=0.1, value=20.0)
            Potasium_Content=st.number_input('Potasium Content (mg/kg)', min_value=0.0, step=0.1, value=20.0)
            Calcium_Carbonate_Content=st.number_input('Carbonates Content (g/kg)', min_value=0.0, step=0.1, value=20.0)
            Calcium_Chloride_PH=st.number_input('Calcium Chloride pH', min_value=0.0, step=0.1, value=20.0)
            Moisture_PH=st.number_input('Moisture pH', min_value=0.0, step=0.1, value=20.0)
            Electrical_Conductivity=st.number_input('Electrical Conductivity (mS/m)', min_value=0.0, step=0.1, value=20.0)
            Organic_Carbon=st.number_input(' Organic Carbon ((g/kg)', min_value=0.0, step=0.1, value=20.0)
            Land_Cover=st.selectbox('Land Cover', Land_cover)
            Land_Description=st.selectbox('Land Description', Land_description )
            Aluminium_Oxalate=st.number_input('Aluminium Oxalate Content (mg/kg)', min_value=0.0, step=0.1, value=20.0)
            Iron_Oxalate=st.number_input('Iron Oxalate Content (mg/kg)', min_value=0.0, step=0.1, value=20.0)
            Depth=st.selectbox('Depth', depth)
            col1, col2, col3,col4= st.columns(4)
            BD1=col1.number_input('Bulk Density(0-10)', min_value=0.0, step=0.1, value=20.0)
            BD2=col2.number_input('Bulk Density(10-20)',min_value=0.0, step=0.1, value=20.0)
            BD3=col3.number_input('Bulk Density(20-30)',min_value=0.0, step=0.1, value=20.0)
            BD4=col4.number_input('Bulk Density(0-20) ',min_value=0.0, step=0.1, value=20.0)
            submitted = st.form_submit_button("Make Prediction")
            if submitted:
                
                import pickle
                scalerfile = 'pkls/Country.pkl'
                scaler = pickle.load(open(scalerfile, 'rb'))
                Country= scaler.transform([Country])
                Country=Country[0]

                scalerfile = 'pkls/Land Cover.pkl'
                scaler = pickle.load(open(scalerfile, 'rb'))
                Land_cover_= scaler.transform([Land_Cover])
                Land_Cover=Land_cover_[0]

                scalerfile = 'pkls/Depth.pkl'
                scaler = pickle.load(open(scalerfile, 'rb'))
                Depth= scaler.transform([Depth])
                Depth=Depth[0]

                scalerfile = 'pkls/Land Description.pkl'
                scaler = pickle.load(open(scalerfile, 'rb'))
                Land_description_= scaler.transform([Land_Description])
                Land_Description=Land_description_[0]


                X=[Country, Phosphorus_Content, Nitrogen_Content, Potasium_Content, Calcium_Carbonate_Content, Calcium_Chloride_PH, Moisture_PH, \
                   Electrical_Conductivity, Organic_Carbon,Land_Cover, Land_Description, Aluminium_Oxalate,  Iron_Oxalate, Depth, BD1, \
                   BD2, BD3, BD4]
                
                

                from catboost import CatBoostClassifier
                model = CatBoostClassifier()
                
                model.load_model('models/Environmental impact')
                pred=model.predict([X][0])
                global env_prediction
                if pred==1:
                    env_prediction='Environmentally Impacted'
                else:
                    env_prediction='Not Environmentally Impacted'


                model.load_model('models/Managed_Unmanged')
                pred=model.predict([X][0])
                global man_prediction_
                if pred==1:
                    man_prediction_='Unmanaged'
                else:
                    man_prediction_='Managed'
                  
                X=np.array(X)
                X=X.reshape(1, -1)
                rf=RandomForestRegressor(random_state=20)

                global rich
                global abund
                
                f = open('pkls/fungi_abd.pkl', 'rb')
                abundance = pickle.load(f)
                abund=abundance.predict([X][0])
                abund=abund[0]
                f.close()

                
                
                f = open('pkls/fungi_rich.pkl', 'rb')
                rich = pickle.load(f)
                rich=rich.predict([X][0])
                rich_=rich[0]
                f.close()


                
                f = open('pkls/bact_abd.pkl', 'rb')
                abundance = pickle.load(f)
                bact_abund=abundance.predict([X][0])
                bact_abund=bact_abund[0]
                f.close()

                
                
                f = open('pkls/bact_rich.pkl', 'rb')
                rich = pickle.load(f)
                bact_rich=rich.predict([X][0])
                bact_rich=bact_rich[0]
                f.close()


               
                
                with st.expander('Model Output'):
            
                    st.dataframe(pd.DataFrame({'Label':['Land Class', 'Soil Class', 'Fungal Abundance*', 'Fungal Richness**', 'Bacteria Abundance*', 'Bacterial Richness**'],\
                              'Values': [man_prediction_, env_prediction, rich_, abund, bact_abund, bact_rich]}))
                st.write("""
                ***Abundance:** The total weighted concentration/abundance of microbiome ooccurence in sample
                """)
                st.write("""
                    ****Richness:** Count of diverse microbiome richness present in the sample
                """)

      








    if testing == "GSMc Model":
        st.subheader('Soil Fungi Richness, Abundance and Trophic-Mode Predictor')
        html_temp = """
        <div style="background-color:#01252C;padding:5px">
        <h2 style="color:white;text-align:center;"> Please input your predictor variables below </h2>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)

        with st.form("my_form"):
            st.markdown('<h2 style="font-size:20px;">NB: Input zero (0) for parameters without values</h1>', unsafe_allow_html=True)
            Last_fire_y_ago=st.number_input('Number of Years Since Last Fire', min_value=1, step=1, value=100)
            nativeness=st.selectbox('Nativeness', ['native', 'non-native'])
            warning=st.selectbox('Warning', ['no concern', 'molds_above_5SD_median', 'non-standard_sampling','contamination_risk'])
            delta15N=st.number_input('Delta15N', min_value=0.0, step=0.1, value=20.0)
            N_conc_g_kg=st.number_input('Nitrogen Conc (g/kg)', min_value=0.0, step=0.1, value=20.0)
            P_conc_mg_kg=st.number_input('Phosphorus Conc (mg/kg)', min_value=0.0, step=0.1, value=20.0)
            Biome=st.selectbox('Biome', ['forest', 'shrubland', 'woodland', 'anthropogenic', 'tundra biome','grassland', 'desert', 'mangrove biome', 'unknown'])
            Biome_specific=st.selectbox('Specific Biome', bs)
        
            submitted = st.form_submit_button("Make Prediction")
            if submitted:
                import pickle
                scalerfile = 'pkls/nativeness.pkl'
                scaler = pickle.load(open(scalerfile, 'rb'))
                nativeness= scaler.transform([nativeness])
                nativeness=nativeness[0]

                scalerfile = 'pkls/warning.pkl'
                scaler = pickle.load(open(scalerfile, 'rb'))
                warning= scaler.transform([warning])
                warning=warning[0]

                scalerfile = 'pkls/Biome.pkl'
                scaler = pickle.load(open(scalerfile, 'rb'))
                Biome= scaler.transform([Biome])
                Biome=Biome[0]

                scalerfile = 'pkls/Biome specific.pkl'
                scaler = pickle.load(open(scalerfile, 'rb'))
                Biome_specific= scaler.transform([Biome_specific])
                Biome_specific=Biome_specific[0]

                X=[Last_fire_y_ago, nativeness, warning, delta15N, N_conc_g_kg, P_conc_mg_kg, Biome, Biome_specific]

                from catboost import CatBoostRegressor
                model = CatBoostRegressor()
                global pred_richness_
                global pred_abundance_
                global Unassigned
                global Saprotroph_Symbiotroph
                global Saprotroph
                global Pathotroph_Saprotroph_Symbiotroph
                global Symbiotroph
                global Pathotroph_Symbiotroph
                global Pathotroph
                global Pathotroph_Saprotroph

                model.load_model('models/ct_richness_global')
                pred_richness=model.predict([X])
                pred_richness_=pred_richness[0]
                model.load_model('models/ct_abundance_global')
                pred_abundance=model.predict([X])
                pred_abundance_=pred_abundance[0]

                model.load_model('models/Unassigned')
                Unassigned=model.predict([X])
                Unassigned=Unassigned[0]
                model.load_model('models/Saprotroph-Symbiotroph')
                Saprotroph_Symbiotroph=model.predict([X])
                Saprotroph_Symbiotroph=Saprotroph_Symbiotroph[0]
                model.load_model('models/Saprotroph')
                Saprotroph=model.predict([X])
                Saprotroph=Saprotroph[0]
                model.load_model('models/Pathotroph-Saprotroph-Symbiotroph')
                Pathotroph_Saprotroph_Symbiotroph=model.predict([X])
                Pathotroph_Saprotroph_Symbiotroph=Pathotroph_Saprotroph_Symbiotroph[0]
                model.load_model('models/Symbiotroph')
                Symbiotroph=model.predict([X])
                Symbiotroph=Symbiotroph[0]
                model.load_model('models/Pathotroph-Symbiotroph')
                Pathotroph_Symbiotroph=model.predict([X])
                Pathotroph_Symbiotroph=Pathotroph_Symbiotroph[0]
                model.load_model('models/Pathotroph')
                Pathotroph=model.predict([X])
                Pathotroph=Pathotroph[0]
                model.load_model('models/Pathotroph-Saprotroph')
                Pathotroph_Saprotroph=model.predict([X])
                Pathotroph_Saprotroph=Pathotroph_Saprotroph[0]

               



                

                with st.expander('Model Output'):
            
                    st.dataframe(pd.DataFrame({'Label':['Fungal Abundance*', 'Fungal Richness**'],\
                                      'Values': [pred_abundance_, pred_richness_]}))
                    st.write("""
                    ***Fungal Abundance:** The total weighted concentration/abundance of Fungal ooccurence in sample
                    """)
                    st.write("""
                    ****Fungal Richness:** Count of diverse Fungal richness present in the sample
                    """)

                    label=['Unassigned', 'Saprotroph-Symbiotroph', 'Saprotroph','Pathotroph-Saprotroph-Symbiotroph', 'Symbiotroph',\
                           'Pathotroph-Symbiotroph', 'Pathotroph', 'Pathotroph-Saprotroph']
                    
                    values=  [Unassigned, Saprotroph_Symbiotroph, Saprotroph,Pathotroph_Saprotroph_Symbiotroph, Symbiotroph,\
                               Pathotroph_Symbiotroph, Pathotroph, Pathotroph_Saprotroph]
                    
                    #st.dataframe(pd.DataFrame({'Label': label, 'Values': values}))
                    
                    import plotly.express as px
                    fig = px.pie(values=values, names=label, title="Predicted Trophic Mode Distribution")
                    st.plotly_chart(fig, use_container_width=True)                
                
                

        with st.sidebar:
            st.image("images/cover.png")
            st.info("""The GSMc model is built using the global soil fungal dataset of the Global Soil Mycobiome consortium (GSMc), to boost further prediction of soil fungal biodiversity, biogeography and macroecology in soil samples. The dataset comprises 722,682 fungal operational taxonomic units (OTUs) from 3200 plots in 108 countries on all continents. The OTUs are taxonomically and functionally assigned to guilds and other functional groups.""")
            st.info("""The GSMc dataset is available [here](https://doi.plutof.ut.ee/doi/10.15156/BIO/2263453)""")
            st.info("""Citation: Tedersoo, Leho (2021): The Global Soil Mycobiome consortium dataset for boosting fungal diversity research v2. University of Tartu. 10.15156/BIO/226345.""")
            
        
   
        
        


import streamlit
from streamlit import runtime
import sys
from streamlit.web import cli as stcli
if __name__ == '__main__':
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())

