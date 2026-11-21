import pywhatkit

mobile = input('enter mobile no of receiver : ')
message = input('enter message you wanna send : ')

pywhatkit.sendwhatmsg_instantly(mobile, message, wait_time=20, tab_close=True)