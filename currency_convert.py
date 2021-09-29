#importing our needed libraries
from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests
import json

#creating our constructor class
class currency_Convert():
    """docstring for ."""
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
    def convert(self,current_To,current_From,amount):
        intial_amount = amount
        #converting initial amount to USD
        if current_From != 'USD':
            self.currencies[current_From]
        #limiting our decimal
        amount = round(amount * self.currencies[current_To],4)
        return amount
#grabbing our api url / constructor
url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = currency_Convert(url)

#converting USDs to Indian Rupee
print(converter.convert('INR','USD',100))
# converting USDs to South African Rand
print(converter.convert('ZAR','USD',300))
