import tfr as tf

if __name__ == "__main__":
    obj_tf = tf.processor
    data = obj_tf.dataprocees()
    graph = obj_tf.mapperprocess(data[0], data[1], data[2])
    graph.show()