#!/bin/bash

# Function to remove files except .conf
remove_files_except_conf() {
  local directory="$1"
  find "$directory" -type f ! -name "*.conf" -delete
  find "$directory" -type d -empty -delete
}

# Directory to search for subfolders
directory=$(pwd)

# Find subfolders with .conf files
subfolders=$(find "$directory" -type f -name "*.conf" -exec dirname {} \;)

# Iterate through the subfolders
for subfolder in $subfolders; do
  remove_files_except_conf "$subfolder"
  echo "Deletion in $subfolder finished."
done
