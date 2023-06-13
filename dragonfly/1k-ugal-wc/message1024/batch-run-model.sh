#!/bin/bash
if [ -n "$1" ]; then
    num="$1"
else
    num=10
fi


echo "MPI rank: $num"

# Define the list of values
values=("0.3")

# Iterate over each value
for value in "${values[@]}"; do
    echo "Executing command with value: $value"

    # Execute the command and capture the output in a text file
    output_file="output_$value.txt"
    mpirun --map-by core -np $num ../../../../build/src/network-workloads/model-net-synthetic-dragonfly-all --synch=3 --warm_up_time=30000 --payload_sz=1024 --lp-io-dir="$output_file" --lp-io-use-suffix=1  --load="$value" --traffic=2 --num_messages=10000 --extramem=300000  -- ./modelnet-test-dragonfly-dally.conf > "$output_file" 2>&1

    # Print the status
    if [ $? -eq 0 ]; then
        echo "Command executed successfully."
    else
        echo "Command execution failed."
    fi

    echo
done
