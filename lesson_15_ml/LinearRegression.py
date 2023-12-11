import numpy as np

class LinearRegression:
    def __init__(
        self,
        x_train: np.ndarray,
        y_train: np.ndarray,
        y: np.ndarray,
        optimizer: str = "SGD",
        loss_function: str = "MSE",
        learning_rate: np.float64 = 0.0005,
        epochs: int = 5000,
        batch_size: int = 1,
    ) -> None:
        """
        optimizers: GD - gradient descent, SGD - stochastic gradient descent, BGD - batch gradient descent
        loss_functions: MSE - mean squared error, MAE - mean absolute error
        """
        self.__x_train: np.ndarray = np.hstack([x_train, np.ones((x_train.shape[0], 1))])
        self.__weights: np.ndarray = np.zeros((self.__x_train.shape[1], 1))
        self.__y_train: np.ndarray = y_train
        self.__y: np.ndarray = y
        self.__optimizer: str = optimizer
        self.__loss_function: str = loss_function
        self.__learning_rate: np.float64 = learning_rate
        self.__epochs: np.int64 = epochs
        self.__batch_size: np.int64 = batch_size
        self.__set_loss_function_and_optimizer()
        self.__run()

    def __set_loss_function_and_optimizer(self) -> None:
        if self.__loss_function == 'MSE':
            self.__loss_function = self.__mse
            self.__loss_function_directive = self.__mse_directive
        elif self.__loss_function == 'MAE':
            self.__loss_function = self.__mae
            self.__loss_function_directive = self.__mae_directive
        else:
            raise TypeError('Invalid loss function')
        
        if self.__optimizer == 'GD':
            self.__optimizer = self.__gradient_descent
        elif self.__optimizer == 'SGD':
            self.__optimizer = self.__stochastic_gradient_descent
        elif self.__optimizer == 'BGD':
            self.__optimizer = self.__batch_gradient_descent
        else:
            raise TypeError('Invalid optimizer')

    def __run(self) -> None:
        self.__train()

    def __train(self) -> None:
        for i in range(self.__epochs):
            gradient = self.__optimizer().reshape(self.__weights.shape)
            self.__weights -= gradient * self.__learning_rate
            if (i + 1) % 10 == 0:
                print(f"Epoch {i + 1} loss_function: {self.__loss_function()}")

    def __gradient_descent(self) -> np.ndarray:
        return -2 / self.__x_train.shape[0] * np.sum((self.__y_train - self.__predict()) * self.__x_train, axis=0)

    def __stochastic_gradient_descent(self) -> np.ndarray:
        index = np.random.randint(0, 5)
        x = self.__x_train[index:index + 1]
        y = self.__y_train[index:index + 1]
        return 2 * x.T.dot(x.dot(self.__weights) - y)

    def __batch_gradient_descent(self) -> np.ndarray:
        indices = np.random.choice(len(self.__x_train), size=self.__batch_size, replace=False)
        return -2 / self.__x_train[indices].shape[0] * np.sum(
            (self.__y_train[indices] - self.__predict()) * self.__x_train[indices], axis=0
        )

    def __predict(self) -> np.ndarray:
        return self.__x_train.dot(self.__weights)

    def __mse(self) -> np.float64:
        return np.mean((self.__y_train - self.__predict()) ** 2)

    def __mae(self) -> np.float64:
        return np.mean(np.abs(self.__predict() - self.__y_train))

    def __mse_directive(self) -> np.ndarray:
        return -2 * np.mean(self.__x_train.T.dot(self.__y_train - self.__predict()))

    def __mae_directive(self) -> np.ndarray:
        return -np.sign(self.__y_train - self.__predict()).dot(self.__x_train)
