Analysis Readme
Steps to Run the Analysis
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
		wget -i *download_links.txt

Check to ensure that all the necessary files have been successfully downloaded.

5. Create Manifest Files
Use the provided manifest.sh files to generate the manifest files required for Qiime2 import.

6. Run Analysis Scripts
Navigate to each directory and execute the analysis.sh files. Before running, review the content of these files to ensure that all necessary files are accounted for and modify the scripts as needed to suit your specific analysis requirements.


#Info

We used the files available from ENA because the AWS bucket wil be shut down soon.
to get the AWS bucket links check the AWS_bucket_links.sh to see the download scripts