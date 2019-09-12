from util import NormalizerProcessor
import numpy as np

def main():
    l = np.random.randn(10,5)
    print(l)
    norp = NormalizerProcessor()
    l2 = norp.process_state_batch(l)
    print(l2)

main()