from LinearRegression import LinearRegression
from LinearRegression import np

def main():
    x_train = np.array([1,2,3,4,5]).reshape(5,-1)
    y_train = np.array([2,3,4,5,6]).reshape(5,-1)
    
    # np.random.seed(33)
    # x_train = np.random.rand(1000,1)
    # x_train = x_train.reshape((-1, 5))
    # params = np.random.rand(5,1)
    # y_train = x_train.dot(params) + 2 + np.random.rand(1)


    LinearRegression(x_train,y_train,[])


if __name__ == '__main__':
    main()