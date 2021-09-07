#WeLeakInfo_API_Request_V4
import requests

email = input("Enter an email that you want to check: ")
# made GET request and stored data in api_call_results
api_call_results = requests.get(
    f'https://api.weleakinfo.to/api?value={email}&type=email&key=IEMF-RJXT-HEBD-ENDQ')

# converted the data in json format(in Python json can be treated as dictionary) and stored in result variable
dict_result = api_call_results.json()

# first check there is any error with the GET request, if success is True then proceed next otherwise shows error
if dict_result['success']:
    # check there is any user data available
    if dict_result['found'] > 0:
        all_data = []  # will store all the data in string as a list
        for each in dict_result['result']:  # loop through each result(dict_result['result'] is a list)
            text = ""  # temp text variable to store text in required structure

            # as each item in dict_result['result'] list is a dictionary so we can get the value using its key
            # split the text based on :(colon), split will return the list. In our
            # case it will return two items in list, the first one is email and other is password
            line = each['line'].split(":")

            text += "Email: "  # added Label to text variable
            text += line[0] + '\n'  # added the user email and a newline escape character to move to the next line

            text += "Password: "  # added Label to text variable
            if len(line) > 1:
                text += line[1] + '\n'  # add the user password and a newline escape character to move to the next line
            else:
                continue

            text += "Source: "  # added Label to text variable

            # check sources are available
            if len(each['sources']) > 0:
                # loop through each sources and added to text variable separated by comma
                for i in range(len(each['sources'])):
                    if i == len(each['sources']) - 1:  # check if there is last element then wont add comma at the end
                        text += each['sources'][i]
                    else:
                        text += each['sources'][i] + ", "
                text += '\n'  # added a newline escape character to move to the next line
            else:
                # added Unknown if there is no source available & a newline escape character to move to the next line
                text += 'Unknown\n'

            text += "-" * 20 + '\n'  # added a newline escape character to move to the next line and

            all_data.append(text)  # added a text variable to all_data list for later use

        result_length = len(all_data)  # get the length of total items available

        print(f"I found something:")

        # print each item in all_data list
        for each in all_data[:3]: #remove [:3] to check data before creating a pastebin
            print(each.strip())

        # check if there are more than 5 items then will proceed the pastebin step
        if result_length > 3:
            text = ""  # created a text variable to convert the list item to string so that it can be used for pastebin
            for each in all_data:
                text += each

            data = {'api_dev_key': 'EiL9ngnoApmKM83C0B88aDE23Ud3uSnN',
                    'api_option': 'paste',  # this will create new paste
                    'api_paste_code': text,  # your actual text you want to paste
                    'api_paste_expire_date': '10M'  # this will make the pastebin link temporary
                    }
            # request to pastebin with cleaned results
            pastebin = requests.post("https://pastebin.com/api/api_post.php", data=data)

            print(
                f"You get the picture so rather than me listing all {result_length} of them here's a link with them all" + pastebin.text)
    else:
        print("I didn't find anything for this email!")
else:
    print("I don't see anything for this.")