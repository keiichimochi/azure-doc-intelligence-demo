from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def analyze_document(document_url):
    # Initialize the client
    endpoint = os.getenv('AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT')
    key = os.getenv('AZURE_DOCUMENT_INTELLIGENCE_KEY')
    
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, 
        credential=AzureKeyCredential(key)
    )

    # Start analysis
    poller = document_analysis_client.begin_analyze_document_from_url(
        "prebuilt-document",
        document_url
    )
    result = poller.result()

    # Process and print results
    for page in result.pages:
        print(f"\nPage {page.page_number}:")
        for line in page.lines:
            print(f"Line: {line.content}")

if __name__ == "__main__":
    # Example usage
    document_url = "YOUR_DOCUMENT_URL"
    analyze_document(document_url)