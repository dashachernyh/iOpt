from iOpt.output_system.listeners.static_painters import StaticPainterListener
from iOpt.output_system.listeners.animate_painters import AnimatePainterListener
from sklearn.datasets import load_breast_cancer
from iOpt.solver import Solver
from iOpt.solver_parametrs import SolverParameters
from examples.Machine_learning.SVC._1D.Problems import SVC_Fixed_Regularization
from sklearn.utils import shuffle
import numpy as np


def load_breast_cancer_data():
    dataset = load_breast_cancer()
    x_raw, y_raw = dataset['data'], dataset['target']
    inputs, outputs = shuffle(x_raw, y_raw ^ 1, random_state=42)
    return inputs, outputs


if __name__ == "__main__":
    x, y = load_breast_cancer_data()
    regularization_value = 6
    kernel_coefficient_bound = {'low': -7, 'up': -3}
    problem = SVC_Fixed_Regularization.SVC_Fixed_Regularization(x, y, regularization_value, kernel_coefficient_bound)

    method_params = SolverParameters(r=np.double(3.0), itersLimit=10, eps=np.double(0.05))
    solver = Solver(problem, parameters=method_params)

    apl = AnimatePainterListener("svc1d_anim.png", "output", toPaintObjFunc=True)
    solver.AddListener(apl)

    spl = StaticPainterListener("svc1d_stat.png", "output", mode="interpolation")
    solver.AddListener(spl)

    solver_info = solver.Solve()
    print(solver_info.numberOfGlobalTrials)
    print(solver_info.numberOfLocalTrials)
    print(solver_info.solvingTime)

    print(solver_info.bestTrials[0].point.floatVariables)
    print(solver_info.bestTrials[0].functionValues[0].value)
