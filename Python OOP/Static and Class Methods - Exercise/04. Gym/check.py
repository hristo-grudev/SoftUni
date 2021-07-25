from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

Customer.id = 1
print(Trainer.id)
print(Customer.get_next_id())