# SATA-ChatBot
Get instant answers to your questions with a chatbot powered by Python, Twilio, Wikipedia, and Wolfram Alpha!

Check out the step-by-step YouTube tutorial [here](https://www.youtube.com/watch?v=hgEiYBjft8A) 

**Here are some examples of what you can do with this program:**

![image](https://user-images.githubusercontent.com/43652410/96490211-84b18280-120e-11eb-9331-90d1917b1f32.png)

To check out the full range of commands you can enter, visit the Wolfram Alpha website [here](https://www.wolframalpha.com/) and Wikipedia API documentation [here](https://wikipedia.readthedocs.io/en/latest/code.html#api)

# Required Installations

- In order to run this program, you will need to follow these steps:

    - Download **pip** if you haven't already, from [here](https://pip.pypa.io/en/stable/installing/)
    - Install **Flask** by running `pip install Flask`
    - Install the **Wikipedia API** by running `pip install wikipedia`
    - Download **Ngrok** [here](https://ngrok.com/)
    - Create a **Twilio** account [here](https://www.twilio.com/try-twilio) and follow the steps to obtain a phone number that you will be sending texts to
        - **Unfortunately, you will have to pay a minimum of $20 to upgrade your account to be able to use the phone number for this project**
        - Read more about sending SMS messages with Twilio [here](https://www.twilio.com/docs/sms/quickstart/python)
        - Once you upgrade your account, run `pip install twilio`
    - Install the **Wolfram Alpha API** by running `pip install wolframalpha`
    
        - Then, sign up for free API access of Wolfram Alpha [here](https://products.wolframalpha.com/api/)
        - Follow the steps accordingly to obtain your AppID
    
# How To Run

   - First, download the zip file containing all the source code and unzip the folder. Then, move the folder to your desktop and rename it to **ChatBot**
   
   - Open the `sata_chatbot.py` file and change the `app_id` variable located on line 70 to your designated Wolfram Alpha AppID.
   
![image](https://user-images.githubusercontent.com/43652410/96471993-f3d2ab00-11fd-11eb-8f5c-2cb4bdfcdbf3.png)
   
   - Run `cd desktop` in terminal to navigate to your desktop directory. Then, run `cd ChatBot` to navigate to that folder and finally run `sata_chatbot.py` to execute the code.
   
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

If you are having any issues running the code, please refer to this link or contact faizan.ahmed18@stjohns.edu. 
    
   - https://makezine.com/projects/sms-bot/
