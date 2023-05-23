import requests # import the module needed

link = input('Discord Invite Link: ')  # get the discord invite link
discordapilink = f"https://discordapp.com/api/v6/invite/{link}" # insert the invite link into the discord api for invites


with open('tokens.txt', "r") as file: # access the file with tokens setting its name as file
    tokens = file.readlines() # begin reading the content within the file
    for x in tokens: # start a for loop so this is repeated
        token = x.rstrip() # remove all white spaces
        header = {
            'Authorization': token
        }    # create a header for the headers we're going to use when sending the request post
        requests.post(discordapilink, headers=header) # send the post request with the given information 
