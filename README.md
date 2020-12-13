In our project, we implement the algorithm for a randomness beacon based on Bitcoin test the output using randomness test recommended by NIST. The results are compared against NIST's randomness beacon.

beacon_collector.py and bitcoin_dataset_collector.py were used to collect data from the NIST beacon and about bitcoin blocks, respectively.

dataset_bitcoin_beacon.py was used to produce random outputs according to the algorithm for our Bitcoin randomness beacon.

data_processor.py and entropy_estimator_preprocess.py were used to convert the collected data to the format used by the tests we carried out.

The test suite used for estimating min-entropy can be found here:
https://github.com/usnistgov/SP800-90B_EntropyAssessment

The tests used for evaluating randomness can be found here:
https://csrc.nist.gov/Projects/Random-Bit-Generation/Documentation-and-Software
