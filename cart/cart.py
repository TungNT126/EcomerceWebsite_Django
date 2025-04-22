from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        # Get current session key
        cart = self.session.get('session_key')

        # If the user is new, no session key, Create new!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages
        self.cart = cart
    
    def add(self, product):
        product_id = str(product.id)

        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Get id from cart
        product_ids = self.cart.keys()
        
        # Use ids to lookup products in DB
        products = Product.objects.filter(id__in=product_ids)
        
        # Return those look above
        return products
