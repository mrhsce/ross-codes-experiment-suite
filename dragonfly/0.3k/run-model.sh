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

mpirun --map-by core -np $num ../../../build/tests/modelnet-test --num_messages=$messages --synch=3  -- ./modelnet-mpi-test-dragonfly.conf #> results.txt
