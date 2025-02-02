from problems.GKLS import GKLS
from iOpt.solver import Solver
from iOpt.solver_parametrs import SolverParameters

from iOpt.output_system.listeners.static_painters import StaticPainterNDListener
from iOpt.output_system.listeners.console_outputers import ConsoleOutputListener


def SolveSingleGKLS():
    """
    Минимизация тестовой функции из GKLS генератора с номером 39
    """

    # создание объекта задачи
    problem = GKLS(2, 39)

    # Формируем параметры решателя
    params = SolverParameters(r=3.5, eps=0.01, itersLimit=300, refineSolution=True)

    # Создаем решатель
    solver = Solver(problem, parameters=params)

    # Добавляем вывод резултатов в консоль
    cfol = ConsoleOutputListener(mode='full')
    solver.AddListener(cfol)

    # Добавляем построение 3D визуализации после решения задачи
    spl = StaticPainterNDListener("GKLS.png", "output", varsIndxs=[0, 1], mode="lines layers", calc="objective function")
    solver.AddListener(spl)

    # Решение задачи
    sol = solver.Solve()


if __name__ == "__main__":
    SolveSingleGKLS()
