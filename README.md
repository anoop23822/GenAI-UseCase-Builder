# Multi-Agent Architecture for AI/GenAI Use Case Generation

This project implements a **Multi-Agent Architecture** to generate AI and **Generative AI (GenAI)** use cases for various companies. The system scrapes industry data, generates relevant AI/ML use cases, and collects relevant datasets for each company. The output is saved in a markdown file that contains company-specific industry insights, generated AI/ML use cases, and dataset links.

## Features:
1. **Industry Research Agent**: Scrapes Google News for industry-specific articles related to the company.
2. **Use Case Generation Agent**: Generates AI/ML use cases based on industry data using the **GPT-2** model.
3. **Dataset Collection Agent**: Collects publicly available datasets from platforms like **Kaggle** and **HuggingFace**.
4. **Final Report Generation**: Saves the results in a markdown file containing research data, use cases, and dataset links.
5. **Downloadable Output**: Provides a downloadable markdown file with the results.

## Installation & Setup

Follow the steps below to set up the environment and run the code.

### Requirements:
1. **Python 3.x**
2. **Google Colab (or local environment)**
3. **Libraries**: You can install the required libraries using the `requirements.txt` file provided.

### Setup Steps:
1. Clone this repository or copy the provided code into a Google Colab notebook.
2. Install the required libraries using `requirements.txt`.
3. Execute the code in the Google Colab notebook or locally to perform the tasks.

### Running the Code:
To run the code, simply call the `main` function with a list of company names. The system will:
- Research the industry for each company.
- Generate AI/ML use cases.
- Collect relevant datasets.
- Save the output in a markdown file that you can download.

Example:
```python
companies = ['Tesla', 'Amazon', 'Google', 'Microsoft', 'Apple']
main(companies)
