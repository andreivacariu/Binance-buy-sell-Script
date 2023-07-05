import customtkinter
import numpy
from binance.client import Client
from binance.enums import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("350x500")

root.title("Buy/Sell Binance App")
client = Client('binance api key', 'binance secret', testnet=False)
print(client.get_account())
def PlaceOrder():
    try:
        print("sending order")
        print(SIDE.get())
        print(coin.get())
        if SIDE.get() == "BUY":
            order = client.create_order(symbol=coin.get()+"USDT",
                                side=SIDE_BUY,
                                type=ORDER_TYPE_MARKET,
                                quantity=amount.get())
        else:
            order = client.create_order(symbol=coin.get()+"USDT",
                                side=SIDE_SELL,
                                type=ORDER_TYPE_MARKET,
                                quantity=amount.get())
        print(order)

    except Exception as e:
        print("An exception occured - {}".format(e))
        return False
    return True


def raise_frame(frame):
    frame.tkraise()
    
mainPage = customtkinter.CTkFrame(master=root)
mainPage.pack(fill="both", expand=True, pady=20,padx=60)

label = customtkinter.CTkLabel(master=mainPage, text="Buy/Sell", font=("Roboto", 24))
label.pack(pady=12, padx=10)

SIDE = customtkinter.StringVar()
side = customtkinter.CTkOptionMenu(master=mainPage, values=[SIDE_BUY, SIDE_SELL], variable=SIDE)
side.pack(pady=12, padx=10)

coin = customtkinter.StringVar()
ticker = customtkinter.CTkOptionMenu(master=mainPage, values=["ADA", "BTC", "BNB","DOGE" ,"ETH", "LTC", "SOL", "XRP"], variable=coin)
ticker.pack(pady=12, padx=10)

amountText = customtkinter.CTkLabel(master=mainPage, text="Quantity", font=("Roboto", 12))
amountText.pack(pady=12, padx=10)
amount = ''
amount = customtkinter.CTkEntry(master=mainPage, placeholder_text="Amount", textvariable=amount)
amount.pack(pady=12, padx=10)


placeOrder = customtkinter.CTkButton(master=mainPage, text="Place Order", command=PlaceOrder)
placeOrder.pack(pady=12, padx=10)

root.mainloop()
