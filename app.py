__pragma__('skip')
document = window = console = fetch = 0 # Prevent complaints by optional static checker
__pragma__('noskip')

async def load_data():
    data_container = document.getElementById("dataContainer")
    txt = document.getElementById("loadingText")
    txt.innerHTML = "Loading ..."


    res = await fetch('https://www.testjsonapi.com/products/')
    data = await res.json()


    main_div = document.createElement('div')
    main_div.className = "container"
    data_container.appendChild(main_div)

    main_child = document.createElement('div')
    main_child.className = "row row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3"
    main_div.appendChild(main_child)

    products = []
    for product in data:
        product_card = f"""
        <div class="col mb-4">
            <div class="card border-secondary">
                <img src={product['product_image']} class="card-img-top" width="300px" height="300px">
                <div class="card-body">
                <h6 class="text-secondary">{product['product_title']}</h6>
                <h5 class="text-dark">{product['product_price']}</h5>
                </div>
            </div>
        </div>
        """
        products.append(product_card)

    main_child.innerHTML = "".join(products)
    txt.innerHTML = ""