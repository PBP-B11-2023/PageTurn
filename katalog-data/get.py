import requests
import pandas as pd

# Your Google Books API key. Replace with your own key.
API_KEY = "AIzaSyDlt5wd631Sk6h240c2bBvl2DksVYXMJik"

# Function to get book info from Google Books API
def get_book_info(row):
    title = row["Name"].replace(" ", "+")
    author = row["Author"].replace(" ", "+")
    try:
        query = f"intitle:{title}+inauthor:{author}"
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if "items" in data and len(data["items"]) > 0:
            item = data["items"][0]
            volume_info = item["volumeInfo"]
            if "id" in item:
                book_id = item["id"]
            else:
                return
            
            if "imageLinks" in volume_info:
                image_url = f"https://books.google.com/books/publisher/content/images/frontcover/{book_id}?fife=w400-h600&source=gbs_api"
            else:
                image_url = "Image not found"

            description = volume_info.get("description", "Description not found")

            return pd.Series({"ImageURL": image_url, "Description": description})

    except Exception as e:
        print(f"Error fetching info for {title} by {author}: {e}")

    return pd.Series({"ImageURL": "Error", "Description": "Error"})

# Read data from CSV file using Pandas
csv_file = "book.csv"  # Replace with your CSV file name
data = pd.read_csv(csv_file)

# Apply the get_book_info function to each row and create new columns with image URLs and descriptions
data[["ImageURL", "Description"]] = data.apply(get_book_info, axis=1)

# Save the updated data back to a CSV file
data.to_csv("book_data_with_info.csv_99.csv", index=False)

print("Data with image URLs and descriptions saved to 'book_data_with_info.csv'")