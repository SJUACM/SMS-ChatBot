# SATA-ChatBot
Get instant answers to your questions with a chatbot powered by Python, Twilio, Wikipedia, and Wolfram Alpha!

Check out the step-by-step YouTube tutorial [here](https://www.youtube.com/watch?v=hgEiYBjft8A) 

**Here are some examples of what you can do with this program:**

![image](https://user-images.githubusercontent.com/43652410/96490211-84b18280-120e-11eb-9331-90d1917b1f32.png)

To check out the full range of commands you can enter, visit the Wolfram Alpha website [here](https://www.wolframalpha.com/) and Wikipedia API documentation [here](https://wikipedia.readthedocs.io/en/latest/code.html#api)

# Required Installations

- In order to run this program, you will need to follow these steps:

    - If you do not have **pip** installed, download it [here](https://pip.pypa.io/en/stable/installing/)
    
    - If you do not have **git** installed, download it [here](https://git-scm.com/downloads)
        
    - Download **Ngrok** [here](https://ngrok.com/)
    
    - Create a **Twilio** account [here](https://www.twilio.com/try-twilio) and follow the steps to obtain a phone number that you will be sending texts to
        - **Unfortunately, you will have to pay a minimum of $20 to upgrade your account to be able to use the phone number for this project**
        - Read more about sending SMS messages with Twilio [here](https://www.twilio.com/docs/sms/quickstart/python)
 
    - Sign up for free API access of **Wolfram Alpha** [here](https://products.wolframalpha.com/api/)
        - Follow the steps accordingly to obtain your AppID
    
# How To Run the Code
       
   - Download all the files `git clone https://github.com/faizancodes/SATA-ChatBot.git`
    
   - Then, run `cd SATA-Chatbot` to navigate to the corresponding folder with all the files you just downloaded and run `pip install -r requirements.txt` to install all the necessary libraries for the program to run  
   
        - If this gives you an error, run `python -m pip install -r requirements.txt` or `py -m pip install -r requirements.txt` and see if that works.
   
   - Open the `sata_chatbot.py` file and change the `app_id` variable located on line 70 to your designated Wolfram Alpha AppID.
   
![image](https://user-images.githubusercontent.com/43652410/96471993-f3d2ab00-11fd-11eb-8f5c-2cb4bdfcdbf3.png)
   
   - Run `sata_chatbot.py` to execute the code.
   
   - When you run the code, your terminal should look like this:
   
   ![image](https://user-images.githubusercontent.com/43652410/96471648-8e7eba00-11fd-11eb-9354-438390e63b05.png)
   
   - Your **Port Number** is highlighted in the yellow box. In my case, it is 5000.
   
   - Next, you want to open up Ngrok and type in `ngrok http (port number)`. **Replace "port number" inside the parentheses with your port number**, in my case it would be `ngrok http 5000`. 
   
   - Your Ngrok should look like this: 
   
   ![image](https://user-images.githubusercontent.com/43652410/96400827-cb1bc880-119f-11eb-8de4-2270c92b17ae.png)
   
   - Next, you want to copy the http address that is highlighted in the yellow box and navigate to your Twilio account screen. 
   
   - Click the “#” on the top left of the screen, then click on your Twilio number, scroll down and **enter the http address into the space that says “A message comes in”, as highlighted in the blue box. And make sure the dropdown is set to “webhook”** 
   
   
   ![image](https://user-images.githubusercontent.com/43652410/96400932-146c1800-11a0-11eb-97ee-5f6d23959d9e.png)
            

   - **Save your changes** and you are now set!
   - Message your Twilio number and test out the program!


# Troubleshooting

If you are having any issues running the code, please refer to this link or contact faizan.ahmed18@stjohns.edu 
    
   - https://makezine.com/projects/sms-bot/
