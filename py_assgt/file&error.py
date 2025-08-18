def process_file():
    """Read a file, process its content, and write to a new file with error handling."""
    while True:
        filename = input("Enter the filename to process: ").strip()
        
        try:
            # Read the input file
            with open(filename, 'r') as input_file:
                content = input_file.read()
            
            # Process the content (convert to uppercase in this example)
            processed_content = content.upper()
            
            # Create output filename
            output_filename = f"processed_{filename}"
            
            # Write to output file
            with open(output_filename, 'w') as output_file:
                output_file.write(processed_content)
            
            print(f"\nSuccess! Processed file saved as '{output_filename}'")
            print(f"Original file had {len(content.split())} words and {len(content)} characters.")
            break
            
        except FileNotFoundError:
            print(f"\nError: The file '{filename}' was not found. Please try again.")
        except PermissionError:
            print(f"\nError: You don't have permission to read '{filename}'. Please try another file.")
        except UnicodeDecodeError:
            print(f"\nError: Could not read '{filename}' as a text file. It may be a binary file.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            print("Please try again with a different file.")

if __name__ == "__main__":
    print("=== File Processing Program ===")
    print("This program will read a file and create a processed version.")
    print("The processed version will be in uppercase.\n")
    process_file()