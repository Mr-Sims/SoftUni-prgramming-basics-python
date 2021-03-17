class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)


    def get_subscription_by_id(self, sub_id):
        subscription = [subscription for subscription in self.subscriptions if sub_id == subscription.id][0]
        return subscription

    def get_customer_by_id(self, customer_id):
        customer = [customer for customer in self.customers if customer_id == customer.id][0]
        return customer

    def get_trainer_by_id(self, trainer_id):
        trainer = [trainer for trainer in self.trainers if trainer_id == trainer.id][0]
        return trainer

    def get_exercise_plan_by_id(self, plan_id):
        plan = [plan for plan in self.plans if plan_id == plan.id][0]
        return plan

    def get_equipment_by_id(self, equipment_id):
        equipment = [equipment for equipment in self.equipment if equipment_id == equipment.id][0]
        return equipment

    def subscription_info(self, subscription_id):
        subscription = self.get_subscription_by_id(subscription_id)
        customer_id = subscription.customer_id
        customer = self.get_customer_by_id(customer_id)
        trainer_id = subscription.trainer_id
        trainer = self.get_trainer_by_id(trainer_id)
        plan_id = subscription.exercise_id
        plan = self.get_exercise_plan_by_id(plan_id)
        equipment_id = plan.equipment_id
        equipment = self.get_equipment_by_id(equipment_id)

        # res = f"{subscription.__repr__()}\n"
        # res += f"{customer.__repr__()}\n"
        # res += f"{trainer.__repr__()}\n"
        # res += f"{equipment.__repr__()}\n"
        # res += f"{plan.__repr__()}\n"
        # return res
        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
