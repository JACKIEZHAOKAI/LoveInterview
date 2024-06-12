# User
# The e-commerce website we are running is backed by a database of items that is displayed on the browsing page. 
# The customer insights team informs us that customers are more likely to buy items that have been viewed recently. 
# Code a solution to improve load times and fetch items that the customer has viewed recently.

# class Cache {
#     def __init__(capacity: Int):
#         pass
    
#     def get(key: Int):
#         pass
# }

class Cache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int):
        if key not in self.cache:
            return None  # Return None or an appropriate value indicating a cache miss
        else:
            # Decode the item from JSON when retrieved
            self.cache.move_to_end(key)
            return json.loads(self.cache[key])

    def put(self, key: int, item):
        # Encode the item to JSON before storing
        encoded_item = json.dumps(item)
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = encoded_item

    def add(self, key: int, item):
        self.put(key, item)


# follow up
# time complexity?

# implementation of OrderedDict?    double linked list
#   access in middle?

# LRU cache safe?

#############################################################
# LP

# difficulte complex problem to solve

# difficulte complex problem to solve, make sotry by my background?





