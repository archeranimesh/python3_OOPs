import contact


class Supplier(contact.Contact):
    def order(self, order):
        print(
            "If this were a real system we would send"
            "{} order to {}".format(order, self.name)
        )
