class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if len(self.customers) < self.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        filtered_customer = [c for c in self.customers if c.id == customer_id][0]
        filtered_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if filtered_dvd in filtered_customer.rented_dvds:
            return f"{filtered_customer.name} has already rented {filtered_dvd.name}"
        if filtered_dvd.is_rented:
            return "DVD is already rented"
        if filtered_customer.age < filtered_dvd.age_restriction:
            return f"{filtered_customer.name} should be at least {filtered_dvd.age_restriction} to rent this movie"
        filtered_customer.rented_dvds.append(filtered_dvd)
        filtered_dvd.is_rented = True
        return f"{filtered_customer.name} has successfully rented {filtered_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        filtered_customer = [c for c in self.customers if c.id == customer_id][0]
        filtered_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if filtered_dvd in filtered_customer.rented_dvds:
            filtered_dvd.is_rented = False
            filtered_customer.rented_dvds.remove(filtered_dvd)
            return f"{filtered_customer.name} has successfully returned {filtered_dvd.name}"
        return f"{filtered_customer.name} does not have that DVD"

    def __repr__(self):
        customers = '\n'.join([c.__repr__() for c in self.customers])
        dvds = '\n'.join([d.__repr__() for d in self.dvds])
        string = customers + '\n' + dvds
        return string
