#!/bin/bash

file_name="codellama-13b.Q4_0.gguf"  
url="https://huggingface.co/TheBloke/CodeLlama-13B-GGUF/blob/main/codellama-13b.Q4_0.gguf" 

# Check if file exists in current directory
if [ -f "$file_name" ]; then
    echo "File $file_name exists."
else
    echo "File $file_name does not exist. Downloading..."
    # Download the file
    if command -v curl &> /dev/null; then
        curl -O "$url"
    elif command -v wget &> /dev/null; then
        wget "$url"
    else
        echo "Error: Neither curl nor wget found. Cannot download the file."
        exit 1
    fi

    # Check if download was successful
    if [ -f "$file_name" ]; then
        echo "File $file_name downloaded successfully."
    else
        echo "Error: File $file_name could not be downloaded."
        exit 1
    fi
fi
