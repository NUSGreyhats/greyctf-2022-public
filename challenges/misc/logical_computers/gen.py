import numpy as np
import torch

flag = "grey{sM0rT_mAch1nE5}"

def tensorize(s : str) -> torch.Tensor:
  return torch.Tensor([(ch >> i) & 1 for ch in list(map(ord, s)) for i in range(8)])

def detensorize(lst : list[int]) -> str:
  ans = ""
  for i in range(0, len(lst), 8):
    acc = 0
    for j in range(8):
      acc += lst[i + j] * (1 << j)
    ans += chr(acc)
  return ans
  

tflag = tensorize(flag)
in_dim = len(tflag)
ones = np.where(tflag == 1)[0]

eqs_size = 8 * in_dim
eqs = [[]] * eqs_size
for i in range(0, eqs_size, 2):
  length = np.random.randint(15, 50)
  eqs[i] = list(np.random.choice(ones, size=length, replace=False))
  if i + 1 == eqs_size: break
  length = np.random.randint(2, 6)
  eqs[i + 1] = list(np.random.choice(list(range(in_dim)), size=length, replace=False))


def batch_and(indices : list[int]) -> int:
  ans = 1
  for ind in indices:
    ans &= int(tflag[ind])
  return ans


class NeuralNetwork(torch.nn.Module):
	def __init__(self, in_dimension, mid_dimension, out_dimension=1):
		super(NeuralNetwork, self).__init__()
		self.layer1 = torch.nn.Linear(in_dimension, mid_dimension)
		self.layer2 = torch.nn.Linear(mid_dimension, out_dimension)

	def forward(self, x):
		x = self.layer1(x)
		x[x <= 0] = -1
		x[x >  0] = 1
		return 1 if int(self.layer2(x)) > 0 else -1

### Try solve
from z3 import *

s = Solver()

ans = [BitVec(str(i), 1) for i in range(in_dim)]

known = tensorize("grey{")
for i in range(len(known)):
  s.add(ans[i] == int(known[i]))

known = tensorize("}")
for i in range(len(known)):
  s.add(ans[i - 8] == int(known[i]))

for i in range(7, len(ans), 8):
  s.add(ans[i] == 0)

for eq in eqs:
  expr = "&".join([("ans[%d]" % i) for i in eq])
  s.add(eval(expr + " == batch_and(eq)"))

if s.check() == sat:
  result = [0] * in_dim
  for i in range(in_dim):
    result[i] = int(str(s.model()[ans[i]]))

  print(detensorize(result))
  if detensorize(result) == flag:
    model = NeuralNetwork(in_dim, eqs_size)
    print(model.layer1.weight.size())
    print(model.layer1.bias.size())
    print(model.layer2.weight.size())
    print(model.layer2.bias.size())

    with torch.no_grad():
      for i in range(eqs_size):
        eq = eqs[i]
        for j in range(in_dim):
          model.layer1.weight[i, j] = 1 if j in eq else 0
        # for j in eq:
        #   # model.layer1.weight[i, j] = 1 if tflag[j] == 1 else -1
        #   model.layer1.weight[i, j] = 1

        model.layer1.bias[i] = -1 * len(eq) + 1
        model.layer2.weight[0, i] = 1 if batch_and(eq) == 1 else -1

      model.layer2.bias[0] = -1 * eqs_size + 1

    print("Done setting up model")
    # print(model.state_dict())

    tflag[tflag == 0] = -1
    print("Try predict: ", model(tflag))

    torch.save(model.state_dict(), "model.pth")
    print("Saved model")
