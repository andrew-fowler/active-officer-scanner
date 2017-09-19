### Summary

This tool can be used to detect changes in registered officers for a provided list of companies.

Running the tool will display the officers that have been added and removed in the time period since the tool was last ran.

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

### TODOs
- Improve CLI usability
- Implement backup / csv output
- Prove compile to exe on windows
- Get code to Kayla
- Get code on Github
- Get Kayla to compile py to Windows executable