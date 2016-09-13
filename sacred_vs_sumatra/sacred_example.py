from sacred import Experiment  # central class of the Sacred framework
from sacred.observers import MongoObserver


ex = Experiment('example_experiment')

ex.observers.append(MongoObserver.create(
    url='127.0.0.1:27017',
    db_name='sacred'
    )
)

import time

@ex.config
def my_config():
    recipient = "world"
    message = "Hello %s!" % recipient

@ex.automain
def my_main(message):
    print(message)

