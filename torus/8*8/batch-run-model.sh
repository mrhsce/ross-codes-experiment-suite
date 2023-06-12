#!/bin/bash
num=10
messages=128


mpirun --map-by core -np $num ../../../build/tests/modelnet-test --synch=3 --payload_sz=25600 --arrival_time=10  --num_messages=100  -- ./modelnet-mpi-test-torus.conf


#echo "MPI rank: $num"
#
## Define the list of values
#values=("0.01" "0.1" "0.2" "0.3" "0.4" "0.5" "0.6" "0.7" "0.8" "0.9" "1")
#
## Iterate over each value
#for value in "${values[@]}"; do
#    echo "Executing command with value: $value"
#
#    # Execute the command and capture the output in a text file
#    output_file="output_$value.txt"
#    mpirun --map-by core -np $num ../../../tests/modelnet-test --synch=3 --warm_up_time=30000 --payload_sz=256 --lp-io-dir="$output_file" --lp-io-use-suffix=1  --load="$value" --traffic=1 --num_messages=10000 --extramem=300000  -- ./modelnet-mpi-test-torus.conf > "$output_file" 2>&1
#
#    # Print the status
#    if [ $? -eq 0 ]; then
#        echo "Command executed successfully."
#    else
#        echo "Command execution failed."
#    fi
#
#    echo
#done