import bardapi

# set your input text
input_text = "what is the weather like in Herzliya, in celsius?"

# Send an API request and get a response. # make sure '_BARD_API_KEY' is in your Env variables.
response = bardapi.core.Bard().get_answer(input_text)
print(response['content'])


# set your __Secure-1PSID value to key as a user env variable: '_BARD_API_KEY' Sign out and sign in back again.
# you may use the below for a temporary workaround is to add the following code :  os.environ['_BARD_API_KEY']='xxxxxxxxxxxx'
# to verify if you env has the key already, print the env variables:  pprint.pprint(dict(os.environ), width=1)
