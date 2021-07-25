class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == subscription.customer_id][0]
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        plan = [p for p in self.plans if p.id == subscription.exercise_id][0]
        equipment = [s for s in self.equipment if s.id == plan.equipment_id][0]

        string = '\n'.join(
            [subscription.__repr__(), customer.__repr__(), trainer.__repr__(), equipment.__repr__(), plan.__repr__()])
        return string
