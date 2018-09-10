
from gym.envs.registration import register

register(
    id='oddoreven-v0',
    entry_point='gym_foo.envs:FooEnv',
)
register(
    id='oddoreven-extrahard-v0',
    entry_point='gym_oddoreven.envs:FooExtraHardEnv',
)
