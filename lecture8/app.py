from flask import Flask,render_template
app=Flask(__name__)

products_dict = {
    "apple": 123.5,
    "iphone": {
        "price": 9999.0,
        "color": "red",
        "inch": 16.3,
        "scale": "iPhone 18 Pro Max",
        "memory": "512GB",
    },
    "huawei": 12999.0,
}

@app.route("/product/<product_name>")
def xxxxxxxxxxx(product_name: str):
    price = products_dict.get(product_name)
    if price is None:
        return "李宏毅 (Hung-yi Lee) received the M.S. and Ph.D. degrees from National Taiwan University (NTU), Taipei, Taiwan, in 2010 and 2012, respectively. From September 2012 to August 2013, he was a postdoctoral fellow in Research Center for Information Technology Innovation, Academia Sinica. From September 2013 to July 2014, he was a visiting scientist at the Spoken Language Systems Group of MIT Computer Science and Artificial Intelligence Laboratory (CSAIL)."
    else:
        return f'商品{product_name}的规格是: {price}'

app.run(port=5001)
