#!/bin/bash

# Create the parent directory
parent_folder="Project"

# Create the Parent Folder, if it not exists
if [ ! -d "$parent_folder" ]; then
	mkdir "$parent_folder"
fi

# the child folders names
folders=("Development" "Documentation" "Domonstration" "PUBLISH")

# Create the each chile folder in the Parent Folder
for folder in "${folders[@]}"; do
	full_path="$parent_folder/$folder"

	if [ ! -d "$full_path" ]; then
		mkdir "$full_path"
		echo "Folder '$full_path' created."
	else
		echo "Folder '$full_path' already exists."
	fi
done
