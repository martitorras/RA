import numpy as np
import cv2

def exercise_1():
    vector = np.zeros(10)
    return vector

def exercise_2():
    vector = np.zeros(10)
    vector[4] = 1.0
    return vector

def exercise_3():
    vector = np.arange(10, 50)
    return vector

def exercise_4():
    vector = np.arange(1, 10)
    vector = vector.reshape((3,3))
    return vector

def exercise_5():
    vector = np.arange(1, 10)
    vector = vector.reshape((3,3))
    return vector

def exercise_6():
    vector = np.arange(1, 10)
    vector = vector.reshape((3,3))
    vector = np.flip(vector, 0)
    return vector

def exercise_7():
    vector = np.identity(3)
    return vector

def exercise_8():
    vector = np.random.random_sample((3,3))
    return vector

def exercise_9():
    vector = np.random.seed(101)
    vector = np.random.randint(0,100,10)
    print(np.mean(vector))
    return vector

def exercise_10():
    vector = np.ones((10, 10))
    vector[1:9, 1:9] = 0.0
    return vector

def exercise_11():
    vector = np.ones((5, 5))
    vector[:] = np.arange(1,6)
    return vector

def exercise_12():
    vector = np.random.seed(123)
    vector = np.random.randint(0,100,9)
    vector = vector.reshape((3,3))
    vector = vector.astype(float)
    return vector

def exercise_15():
    np.random.seed(123)
    vector = np.random.random_sample((5,5))
    index = (np.abs(vector-0.5)).argmin()
    print(index)
    return vector

def exercise_16():
    vector = np.random.randint(1,11,(3,3))
    return len(vector[vector > 5])

def exercise_17():
    array = np.arange(0, 256)
    vector = np.zeros(64,64)
    cv2.imshow("will this work?", vector)
    k = cv2.waitKey(0) 
    if k == 27:
        cv2.destroyAllWindows()
    return vector

arr = exercise_17()
print(arr)