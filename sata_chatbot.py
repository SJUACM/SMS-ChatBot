#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to formulate a response based on message input.
def getReply(message):
    
    # Make the message lower case and without spaces on the end for easier handling
    message = message.lower().strip()
    
    # This is the variable where we will store our response
    answer = ""
            
        
    # is the keyword "wolfram" in the message? Ex: "wolfram integral of x + 1"
    if "wolfram" in message:
       
        message = message.replace('wolfram', '')
        
        # Instance of wolfram alpha client class
        client = wolframalpha.Client(app_id) 
        
        # Stores the response from wolfram alpha
        res = client.query(message) 
        
        try:
            # Includes only text from the response 
            answer = next(res.results).text
            
        except:
            answer = 'Sorry, there was an error processing your message. Please try again.'
    
    
    # is the keyword "wiki" in the message? Ex: "wiki LeBron James"
    elif "wiki" in message:
        
        # remove the keyword "wiki" from the message
        message = message.replace('wiki', '')
        
        # Get the wikipedia summary for the request
        try:
            answer = wikipedia.summary(message, sentences=5)
            
        except:
           
            # handle errors or non specificity errors 
            answer = "Request was not found using wiki. Be more specific?"


    # the message contains no keyword. Display a help prompt to identify possible commands
    else:
        answer = "\n Welcome!\nThese are the commands you may use: \nwolfram \"wolframalpha request\" \nwiki \"wikipedia request""\n"
    
    
    # return the formulated answer
    return answer


# In[ ]:


# import all the libraries we will be using
from flask import Flask, request
import wikipedia
import wolframalpha 
from twilio.twiml.messaging_response import Message, MessagingResponse

app_id = 'INSERT_WOLFRAM_APP_ID_HERE' 

# set up Flask to connect this code to the local host, which will
# later be connected to the internet through Ngrok
app = Flask(__name__)
    
# Main method. When a POST request is sent to our local host through Ngrok 
# (which creates a tunnel to the web), this code will run. The Twilio service # sends the POST request - we will set this up on the Twilio website. So when # a message is sent over SMS to our Twilio number, this code will run
@app.route('/', methods=['POST'])
def sms():
    
    # Get the text in the message sent
    message_body = request.form['Body']
    
    # Create a Twilio response object to be able to send a reply back (as per # Twilio docs)
    resp = MessagingResponse()
    
    # Send the message body to the getReply message, where 
    # we will query the String and formulate a response
    replyText = getReply(message_body)

    # Text back our response!
    resp.message(replyText)
    return str(resp)

# when you run the code through terminal, this will allow Flask to work
if __name__ == '__main__':
    app.run()

