from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
# from kivy.core.window import Window
from kivy.config import Config
import requests
from bs4 import BeautifulSoup

# Window.size = (480, 853)

Config.set('graphics', 'fullscreen', True)
Config.write()
Config.set('kivy', 'keyboard_mode', 'systemanddock')


def get_amount(amount):
    res = requests.get('https://minfin.com.ua/currency/crypto/')
    soup = BeautifulSoup(res.text, 'html.parser')
    block = soup.find_all('span', {'class': 'coin-price--num'})[0:5]
    bitcoin = block[0].text
    ethereum = block[1].text
    xrp = block[2].text
    tether = block[3].text
    bitcoin_cash = block[4].text
    bitcoin = bitcoin.replace("USD", '')
    bitcoin = bitcoin.replace(" ", '')
    bitcoin = bitcoin.replace(",", '.')
    ethereum = ethereum.replace("USD", '')
    ethereum = ethereum.replace(" ", '')
    ethereum = ethereum.replace(",", '.')
    xrp = xrp.replace("USD", '')
    xrp = xrp.replace(" ", '')
    xrp = xrp.replace(",", '.')
    tether = tether.replace("USD", '')
    tether = tether.replace(" ", '')
    tether = tether.replace(",", '.')
    bitcoin_cash = bitcoin_cash.replace("USD", '')
    bitcoin_cash = bitcoin_cash.replace(",", '.')
    bitcoin = float(bitcoin)
    ethereum = float(ethereum)
    xrp = float(xrp)
    tether = float(tether)
    bitcoin_cash = float(bitcoin_cash)
    bitcoin = bitcoin * amount
    ethereum = ethereum * amount
    xrp = xrp * amount
    tether = tether * amount
    bitcoin_cash = bitcoin_cash * amount
    bitcoin = f"{bitcoin} USD"
    ethereum = f"{ethereum} USD"
    xrp = f"{xrp} USD"
    tether = f"{tether} USD"
    bitcoin_cash = f"{bitcoin_cash} USD"
    return {'bitcoin': bitcoin, 'ethereum': ethereum,
            'xrp': xrp, 'tether': tether, 'bitcoin_cash': bitcoin_cash}


class Container(GridLayout):
    def calculate(self):
        try:
            amount1 = float(self.text_input.text)
        except:
            amount1 = 0

        crypto = get_amount(amount1)
        self.bitcoin.text = crypto.get('bitcoin')
        self.ethereum.text = crypto.get('ethereum')
        self.xrp.text = crypto.get('xrp')
        self.tether.text = crypto.get('tether')
        self.bitcoin_cash.text = crypto.get('bitcoin_cash')


class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
