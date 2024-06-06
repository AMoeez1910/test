class Product:
    def __init__(self, title, total_reviews, price, image_url, creation_timestamp, update_timestamp):
        self.title = title
        self.total_reviews = total_reviews
        self.price = price
        self.image_url = image_url
        self.creation_timestamp = creation_timestamp
        self.update_timestamp = update_timestamp
    def to_dict(self):
        return {
            'title': self.title,
            'total_reviews': self.total_reviews,
            'price': self.price,
            'image_url': self.image_url,
            'creation_timestamp': self.creation_timestamp,
            'update_timestamp': self.update_timestamp
        }