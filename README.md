# LLM_TEXT_GENERATION

# AI-Powered Question Answering Tool

# Overview

This tool is a web-based application that utilizes a pre-trained language model to answer user questions. Built with Django, it integrates the Hugging Face API to generate responses, providing a seamless user experience.

The application is designed for simplicity, featuring a clean frontend interface for interacting with the model and a robust backend for handling requests

# Features

Accepts user queries through a responsive web interface.

Integrates with Hugging Face's model API for natural language generation.

Supports API key management via environment variables for security.

Lightweight and easy to deploy.

# Setup and Installation
# Prerequisites

Python 3.10 or higher

Git

A Hugging Face account and API key

Django installed on your system

# Step 1: Clone the Repository
git clone https://github.com/TALAVIYAJAY/LLM_TEXT_GENERATION.git

cd LLM_TEXT_GENERATION

# Step 2: Set Up a Virtual Environment
python -m venv env

source env/bin/activate    # For macOS/Linux

env\Scripts\activate       # For Windows

# Step 3: Install Dependencies
pip install -r requirements.txt

# Step 4: Set Up Environment Variables
Add your Hugging Face API key in .env file

# Step 5: Run Database Migrations
python manage.py migrate

# Step 6: Start the Server
python manage.py runserver

# Step 7: Access the Application
Open your web browser and navigate to http://127.0.0.1:8000.

# Example Input/Output
Input: What is the Pythagorean theorem?

Output: The Pythagorean theorem states that in a right triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides.

# Deployed Tool
The application is also deployed for public access. You can try it here:

https://huggingface.co/spaces/STREAK7744/gpt_neo_2.7B

