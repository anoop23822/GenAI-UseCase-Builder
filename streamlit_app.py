import streamlit as st
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from google.colab import files

# Function to research the industry or company by scraping Google News
def research_industry(company_name):
    query = f"{company_name} industry trends"
    search_url = f"https://news.google.com/search?q={query}&hl=en-IN&gl=IN&ceid=IN%3Aen"

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting article titles and links from Google News
    articles = []
    for result in soup.find_all('article'):
        headline = result.find('h3')
        if headline:
            title = headline.get_text()
            link = result.find_parent('a')['href']
            articles.append({'title': title, 'link': 'https://news.google.com' + link})

    return articles

# Function to generate use cases using HuggingFace's pre-trained models (free models)
def generate_use_cases(industry_data):
    generator = pipeline('text-generation', model='gpt2')  # GPT-2 (free to use)
    
    # Creating a prompt from the industry data to generate relevant use cases
    prompt = f"Given the industry trends and technologies in the following data, propose some AI/ML use cases: {industry_data}"
    
    # Generate use cases using GPT-2
    use_case_text = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
    return use_case_text

# Function to collect publicly available datasets (from Kaggle and HuggingFace)
def collect_datasets():
    datasets = {
        'Kaggle': 'https://www.kaggle.com/datasets',
        'HuggingFace': 'https://huggingface.co/datasets',
    }
    return datasets

# Function to handle file download
def save_and_download_file(companies_list):
    with open("companies_use_cases_and_datasets.md", 'w') as file:
        for company_name in companies_list:
            file.write(f"\n## Industry Research for {company_name}:\n")
            industry_data = research_industry(company_name)
            for article in industry_data:
                file.write(f"- {article['title']} [{article['link']}]\n")

            industry_info = " ".join([article['title'] for article in industry_data])  # Concatenating article titles as context
            use_cases = generate_use_cases(industry_info)
            file.write(f"\n## Generated AI/ML Use Cases for {company_name}:\n{use_cases}\n")

            datasets = collect_datasets()
            file.write(f"\n## Datasets for {company_name}:\n")
            for source, link in datasets.items():
                file.write(f"- [{source}]({link})\n")
    
    # Provide a download link
    st.download_button(
        label="Download Results",
        data=open("companies_use_cases_and_datasets.md", "rb").read(),
        file_name="companies_use_cases_and_datasets.md",
        mime="text/markdown"
    )

# Streamlit app UI
st.title('AI/GenAI Use Case Generator')
st.subheader("Generate AI/GenAI Use Cases and Datasets for Multiple Companies")

companies_input = st.text_area("Enter company names (comma separated):", 
                              "Tesla, Amazon, Google, Microsoft, Apple")
companies_list = [company.strip() for company in companies_input.split(',')]

if st.button('Generate Use Cases and Datasets'):
    st.write("Generating use cases and collecting datasets for the companies...")
    save_and_download_file(companies_list)
    st.write("Processing complete! Click the button below to download the results.")
