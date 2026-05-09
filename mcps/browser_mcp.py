import requests

def fetch_celebrity_text(name):
    try:
        # Search Wikipedia first to get correct page title
        search_url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={name}&limit=1&format=json"
        search_response = requests.get(search_url)
        
        if search_response.status_code == 200:
            search_data = search_response.json()
            if search_data[1]:  # if results found
                correct_title = search_data[1][0].replace(' ', '_')
                print(f"Found Wikipedia title: {correct_title}")
                
                # Now fetch full page
                page_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={correct_title}&prop=extracts&explaintext=true&format=json"
                page_response = requests.get(page_url)
                
                if page_response.status_code == 200:
                    pages = page_response.json().get("query", {}).get("pages", {})
                    for page_id, page in pages.items():
                        if page_id != "-1":
                            extract = page.get("extract", "")
                            if extract:
                                print(f"Wikipedia data fetched successfully!")
                                return extract

        return None

    except Exception as e:
        print(f"Error: {e}")
        return None