import os, re, csv
from collections import defaultdict

def calculate_max_rss(file_path):
    # Function to parse the RSS values from the input
    def parse_rss(line):
        try:
            rss_value = line.split()[6]
            return int(rss_value)
        except (ValueError, IndexError):
            return 0

    # Initialize a dictionary to store the sum of RSS for each UID group
    rss_sum_by_uid = defaultdict(int)
    max_rss = 0

    # Read the input from the file
    with open(file_path, 'r') as file:
        # Iterate over the lines in the file and calculate the sum of RSS for each UID group
        current_uid = None
        for line in file:
            line = line.strip()
            if line.startswith(' '):
                # Skip lines that don't start with UID (assume they are not part of the process group)
                continue
            line_parts = line.split()
            if len(line_parts) < 2:
                # Skip lines that don't have enough elements
                continue
            uid = line_parts[1]
            if current_uid is not None and uid != current_uid:
                # Update the max RSS value if necessary
                max_rss = max(max_rss, rss_sum_by_uid[current_uid])
                # Reset the sum for the new UID group
                rss_sum_by_uid[current_uid] = 0
            current_uid = uid
            rss_sum_by_uid[current_uid] += parse_rss(line)

    return max_rss

def extract_parameters(content):
    parameters = {}

    # Extract Running Time
    running_time_match = re.search(r'Running Time\s+=\s+(\d+\.\d+)', content)
    parameters['Running Time'] = running_time_match.group(1) if running_time_match else "Not found"

    # Extract Efficiency
    efficiency_match = re.search(r'Efficiency\s+([\d.]+)\s+%', content)
    parameters['Efficiency'] = efficiency_match.group(1) if efficiency_match else "Not found"

    # Extract hops traversed
    hops_traversed_match = re.search(r'Average number of hops traversed\s+(\d+\.\d+)', content)
    parameters['Hops Traversed'] = hops_traversed_match.group(1) if hops_traversed_match else "Not found"

    # Extract average chunk latency
    avg_chunk_latency_match = re.search(r'average chunk latency\s+(\d+\.\d+)', content)
    parameters['Average Chunk Latency'] = avg_chunk_latency_match.group(1) if avg_chunk_latency_match else "Not found"

    # Extract maximum chunk latency
    max_chunk_latency_match = re.search(r'maximum chunk latency\s+(\d+\.\d+)', content)
    parameters['Maximum Chunk Latency'] = max_chunk_latency_match.group(1) if max_chunk_latency_match else "Not found"

    # Extract Total packets generated
    total_packets_generated_match = re.search(r'Total packets generated\s+(\d+)', content)
    parameters['Total Packets Generated'] = total_packets_generated_match.group(1) if total_packets_generated_match else "Not found"

    # Extract Total packets finished
    total_packets_finished_match = re.search(r'finished\s+(\d+)', content)
    parameters['Total Packets Finished'] = total_packets_finished_match.group(1) if total_packets_finished_match else "Not found"

    return parameters

def search_subdirectories(directory):
    with open('./output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Directory', 'Ram', 'Execution time', 'Efficiency', 'hops', 'avg chunk latency', 'max chunk latency', 'Packets generated', 'Packets finished'])

        for root, dirs, files in os.walk(directory):
            if 'results.txt' in files:
                result_file = os.path.join(root, 'results.txt')
                directory_name = os.path.basename(root)

                with open(result_file, 'r') as file:
                    content = file.read()
                extracted_parameters = extract_parameters(content)

                # Retrieve individual parameters
                running_time = round(float(extracted_parameters['Running Time']),3)
                max_memory = calculate_max_rss(os.path.join(root, 'cpu_RAM.txt'))
                efficiency = extracted_parameters['Efficiency']
                hops_traversed = round(float(extracted_parameters['Hops Traversed']), 2)
                avg_chunk_latency = round(float(extracted_parameters['Average Chunk Latency']) * 1000)
                max_chunk_latency = round(float(extracted_parameters['Maximum Chunk Latency']) * 1000)
                total_packets_generated = extracted_parameters['Total Packets Generated']
                total_packets_finished = extracted_parameters['Total Packets Finished']

                # Print the extracted values
                # print("Running Time:", running_time)
                # print("Max ram usage:", max_memory)
                # print("Efficiency:", efficiency)
                # print("Hops Traversed:", hops_traversed)
                # print("Average Chunk Latency:", avg_chunk_latency)
                # print("Maximum Chunk Latency:", max_chunk_latency)
                # print("Total Packets Generated:", total_packets_generated)
                # print("Total Packets Finished:", total_packets_finished)
                writer.writerow([directory_name, max_memory, running_time, efficiency, hops_traversed, avg_chunk_latency, max_chunk_latency, total_packets_generated, total_packets_finished])


# Example usage:
current_directory = os.getcwd()
search_subdirectories(current_directory)
