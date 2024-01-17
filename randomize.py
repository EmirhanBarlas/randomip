import random

def generate_random_ip():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip

def write_ips_to_file(file_path, num_ips=100):
    with open(file_path, 'w') as file:
        for _ in range(num_ips):
            random_ip = generate_random_ip()
            file.write(random_ip + '\n')

if __name__ == "__main__":
    file_path = 'random_ips.txt'
    write_ips_to_file(file_path, num_ips=100)
    print(f"{file_path} 100 random IP addresses were saved in the file.")