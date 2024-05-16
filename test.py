import tensorflow as tf
import tensorflow.contrib.eager as tfe
 
tfe.enable_eager_execution()   # fungsi untuk menjalankan eager execution
 
def square(vektor):
    result = vektor ** 2
    print(result)
    return result
    
vektor = tf.constant([1.0, 2.0, 3.0, 4.0])
square(vektor)