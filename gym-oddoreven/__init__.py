
from gym.envs.registration import register

register(
    id='oddoreven-v0',
    entry_point='gym_oddoreven.envs:oddoreven_env',
)
