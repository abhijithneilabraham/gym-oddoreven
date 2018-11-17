from gym.envs.registration import registry, register, make, spec

# Algorithmic
# ----------------------------------------
register(
    id='oddoreven-v0',
    entry_point='gym.envs.gym_oddoreven.envs.oddoreven_env',
    max_episode_steps=200,
    reward_threshold=25.0,
)
