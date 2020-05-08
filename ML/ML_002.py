import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)

node3 = tf.add(node1, node2) # node3 = node1 + node2.

@tf.function
def adder_node(a, b):
    return a + b

print([node1, node2])
print(node3)

node4 = tf.constant([1, 3], tf.float32)
node5 = tf.constant([2, 4], tf.float32)

print(adder_node(node4, node5))