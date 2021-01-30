from slack import RTMClient
import requests
from stock import StockData


stock = StockData()
print(stock)



@RTMClient.run_on(event="message")
def marketbot(**payload):
    """
    This function triggers when someone sends
    a message on the slack
    """
    stock = StockData()
    print(stock)
    

    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")

    # If a message is not send by the bot
    if bot_id == "":
        channel_id = data["channel"]

        # Extracting message send by the user on the slack
        text = data.get("text", "")
        text = text.split(">")[-1].strip()

        response = ""
        if "stock-markets" in text.lower():
            
            user = data.get("user", "")
            
            
            response =  f"<@{user}> has requested the market update {stock}"


        web_client.chat_postMessage(channel=channel_id, text=response)

try:
    rtm_client = RTMClient(token="Your-Slack-API-Token")
    print("Bot is up and running!")
    rtm_client.start()
except Exception as err:
    print(err)
