#!/bin/bash
num=10
messages=128

# Check if a value is provided as command line argument
if [[ $# -gt 0 ]]; then
    num=$1
fi

if [[ $# -gt 1 ]]; then
    messages=$2
fi

echo "MPI rank: $num"

#mpirun --map-by core -np $num ../../../build/tests/modelnet-test --num_messages=$messages --synch=3  -- ./modelnet-mpi-test-dragonfly.conf #> results.txt
mpirun --map-by core -np $num ../../../build/src/network-workloads/model-net-synthetic-dragonfly-all --synch=3 --warm_up_time=30000 --payload_sz=256 --lp-io-dir="output" --lp-io-use-suffix=1  --load=0.5 --num_messages=10000 --extramem=300000  -- ./modelnet-test-dragonfly-dally.conf #> results.txt
#mpirun --map-by core -np $num ../../../build/src/network-workloads/model-net-synthetic-dragonfly-all --synch=3 --warm_up_time=30000 --sampling-end-time=10  --arrival_time=2  --num_messages=500  -- ./modelnet-test-dragonfly-dally.conf #> results.txt
