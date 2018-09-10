import gym
from gym import error, spaces, utils
from gym.utils import seeding

class OddorevenEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self,small=2,large=10):
    self.input[]
    self.state=0
    self.seed=0#I am specifying the reard small as 2 and large as 10

  def seed(self, seed=None):
    self.np_random, seed = seeding.np_random(seed)
    return [seed]    
   
  
  def _step(self, action):
    if self.episodes
    
  def _reset(self):
    
  def _render(self, mode='human', close=False):
    
