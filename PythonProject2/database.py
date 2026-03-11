import sqlite3


def lookup_product(barcode):

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, price FROM products WHERE barcode=?",
        (barcode,)
    )

    product = cursor.fetchone()

    conn.close()

    return product