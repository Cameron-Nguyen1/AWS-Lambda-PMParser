# AWS-Lambda-PMParser
## The goal of the program is to allow for quick, abbreviated searches of keywords across programmatically accessible content on pubmed/pubmed central databases.

### Notice the Python 3.9 layer in the Python subdirectory. 
### I included the layer only because it includes downloaded stopwords for the english language used by the NLP algorithm.

This program is meant to work on AWS Lambda, you'll need to provide an email to receive notifications from NCBI with.
Of course you should add your Lambda functions link to the action of the HTML forms.

Here's an example of some parsed articles I searched on the Pubmed database with keywords "Mouse" and "SARS"
![image](https://github.com/user-attachments/assets/a93be634-3308-462b-b618-f2455df90e25)
