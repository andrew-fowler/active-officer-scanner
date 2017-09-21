### Summary

This tool can be used to detect changes in registered officers for a provided list of companies.

Running the tool will display the officers that have been added and removed in the time period since the tool was last ran.

### Usage
1) Modify `resources/Companies House Numbers.csv` file to contain the names and Companies House IDs of the companies you wish to query.
2) Run the tool to establish the original baseline data.  This will be saved to `data/fresh_data.json`, and is viewable as a text file.
3) When you want to recheck the data on Companies House, simply re-run the tool from the Windows command line and it will output the added and removed active officers, and establish a new baseline ready for the next execution.

### Configuration

To connect to the Companies House API, you need to have an active access token.

See https://developer.companieshouse.gov.uk/api/docs/index/gettingStarted/apikey_authorisation.html for more information.

Once you have an access token, you need to create an environment variable for it with the name ACCESS_TOKEN.

See https://www.youtube.com/watch?v=bEroNNzqlF4 for more information.

If you would like to set it via the Windows command line, open a command prompt and execute the following command:

`setx ACCESS_TOKEN "YOUR API KEY" /m`
 
for example: 
 
`setx ACCESS_TOKEN "qoEFZXjs_0Kd75kOonFrS-A397zMB_OJF9iSmwYR" /m` 

then run the program.

### Code maintenance

To create a new distribution/installation after making changes, run `pyinstaller app.py` and it should create a new Windows application under `/dist/`.
