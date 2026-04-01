import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        sig_ans = [0.0]*len(z)
        for i in range(len(z)):
            sig_ans[i] = np.round(1/(1+math.exp(-z[i])),5)
        return sig_ans

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        relu_ans = [0.0]*len(z)
        for i in range(len(z)):
            relu_ans[i] = max(0.0,z[i])
        return relu_ans
