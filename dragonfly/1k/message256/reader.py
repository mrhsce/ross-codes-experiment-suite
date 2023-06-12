import os

directory = "."  # Replace with the path to your directory

# Get the list of text files in the directory
files = [filename for filename in os.listdir(directory) if filename.endswith(".txt")]
sorted_files = sorted(files)

chunk_latency_list = []
message_latency_list = []

# Iterate over the sorted file names
for filename in sorted_files:
    file_path = os.path.join(directory, filename)
    with open(file_path, "r") as file:
        content = file.read()
        latency_start = content.find("average chunk latency") + len("average chunk latency")
        latency_end = content.find("us", latency_start)
        latency = content[latency_start:latency_end].strip()

        message_latency_start = content.find("Mean Message Latency:") + len("Mean Message Latency:")
        message_latency_end = content.find("us", message_latency_start)
        message_latency = content[message_latency_start:message_latency_end].strip()

        print(f"File: {filename}")
        print(f"Average Chunk Latency: {latency} us")
        print(f"Mean Message Latency: {message_latency} us")
        print("-----------------------------")

        chunk_latency_list.append(round(float(latency) * 1000))
        message_latency_list.append(round(float(message_latency) * 1000))

print("chunk_latency_list = " + str(chunk_latency_list))
print("message_latency_list = " + str(message_latency_list))       
