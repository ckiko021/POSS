from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import winsound
from receipt import generate_receipt

from scanner import scan_barcode
from database import lookup_product


class POSLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.cart = []
        self.total = 0

        title = Label(text="PYTHON POS SYSTEM", size_hint=(1, 0.1))
        self.add_widget(title)

        self.product_list = GridLayout(cols=2, size_hint=(1, 0.6))
        self.add_widget(self.product_list)

        self.total_label = Label(text="TOTAL: 0", size_hint=(1, 0.1))
        self.add_widget(self.total_label)

        button_layout = BoxLayout(size_hint=(1, 0.2))

        scan_button = Button(text="SCAN PRODUCT")
        scan_button.bind(on_press=self.scan_product)

        checkout_button = Button(text="CHECKOUT")

        button_layout.add_widget(scan_button)
        button_layout.add_widget(checkout_button)

        self.add_widget(button_layout)

    def scan_product(self, instance):

        barcode = scan_barcode()

        if not barcode:
            return

        product = lookup_product(barcode)

        if product:

            name, price = product
            winsound.Beep(1000, 200)
            self.cart.append(product)
            self.total += price

            self.product_list.add_widget(Label(text=name))
            self.product_list.add_widget(Label(text=str(price)))

            self.total_label.text = f"TOTAL: {self.total}"

    def checkout(self, instance):

        generate_receipt(self.cart, self.total)

        self.cart = []
        self.total = 0

        self.product_list.clear_widgets()

        self.total_label.text = "TOTAL: 0"





class POSApp(App):
    def build(self):
        return POSLayout()