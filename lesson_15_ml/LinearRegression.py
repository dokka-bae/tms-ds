import numpy as np


class LinearRegression:
    def __init__(
        self,
        x_train: np.ndarray,
        y_train: np.ndarray,
        y: np.ndarray,
        optimizer: str = "SGD",
        loss_function: str = "MSE",
        learning_rate: np.float64 = 0.01,
        epochs: int = 100,
        batch_size: int = 1,
    ) -> None:
        """
            optimizers: GD - gradient descent, SGD - stochastic gradient descent, MNSGD - mini-batch stochastic gradient
            loss_functions: MSE - mean squad error, MAE - mean absolute error
        """
        self.__weigths: np.ndarray = np.random.rand(x_train.shape[1])
        self.__x_train: np.ndarray = x_train
        self.__y_train: np.ndarray = y_train
        self.__y: np.ndarray = y
        self.__optimazer: str = optimizer
        self.__loss_function: str = loss_function
        self.__learning_rate: np.float64 = learning_rate
        self.__epochs: np.int64 = epochs
        self.__batch_size: np.int64 = batch_size
        self.__run()

    def __run(self) -> None:
        pass

    def __train(self) -> None:
        pass

    def __gradient_descent(self) -> None:
        pass

    def __stochastic_gradient_descent(self) -> None:
        pass

    def __mini_batches_stochastic_gradient_descent(self, batch_size=1) -> None:
        pass

    def __mse(self, y_pred: np.ndarray) -> np.float64:
        return np.mean(np.sum((y_pred - self.__y) ** 2))

    def __mae(self, y_pred: np.ndarray) -> np.float64:
        return np.mean(np.sum(np.abs(y_pred - self.__y)))

    def __mse_directive(self, y_pred: np.ndarray) -> np.float64:
        return -2 * np.mean(np.sum(self.__x_train - self.__y))

    def __mae_directive(self, y_pred: np.ndarray) -> np.float64:
        pass
