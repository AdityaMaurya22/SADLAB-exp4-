import os
import subprocess

def get_user_input():
    # Vulnerability: No input sanitization leading to command injection risk
    user_input = input("Enter a filename to read: ")
    return user_input

def read_file(filename):
    try:
        # Vulnerability: Using user input directly in system call (command injection)
        output = subprocess.check_output(f"cat {filename}", shell=True, text=True)
        print(output)
    except Exception as e:
        print(f"Error: {e}")

def unsafe_deserialization(data):
    import pickle
    # Vulnerability: Deserializing untrusted input, could lead to code execution
    obj = pickle.loads(data)
    print("Deserialized object:", obj)

def main():
    filename = get_user_input()
    read_file(filename)

    # Example unsafe deserialization (simulated with hardcoded malicious data)
    malicious_data = b"cos\nsystem\n(S'echo Vulnerable to pickle RCE!'\ntR."
    unsafe_deserialization(malicious_data)

if __name__ == "__main__":
    main()
