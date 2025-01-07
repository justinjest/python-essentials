
# **Lesson 09 — Introduction to Web Scraping**

## **Lesson Overview**
**Learning objective:** In this lesson, students will gain a comprehensive understanding of web scraping, focusing on the fundamentals such as HTML structure, DOM representation, and using Python libraries like `BeautifulSoup` and `Requests` to scrape and extract data from web pages. Additionally, students will explore the ethical aspects of web scraping, including adhering to guidelines provided by `robots.txt` and managing server requests responsibly.

### **Topics:**
1. Basics of HTML and DOM
2. Web Scraping Tools: `Requests` and `BeautifulSoup`
3. Ethical Web Scraping: Understanding `robots.txt` and ethical considerations
4. Scraping Structured Data: Extracting specific data points
5. Managing Requests: Delays, retries, and handling errors
6. Saving Scraped Data to Files

---

## **9.1 Basics of HTML and DOM**

### **Overview**
HTML (Hypertext Markup Language) is the backbone of web pages, providing structure and content. The Document Object Model (DOM) is a tree structure that represents the page content. Understanding the structure of web pages and the DOM is essential for locating and extracting data during web scraping.

### **Key HTML Elements:**
- **`<title>`**: The title of the page.
- **`<p>`**: Paragraphs of text.
- **`<h1>, <h2>, <h3>`**: Headers of varying levels.
- **`<a>`**: Links with `href` attributes pointing to URLs.
- **`<img>`**: Images with `src` attributes indicating the image source.

### **Hands-On Activity:**
1. Open the Wikipedia page for "Web Scraping" ([Wikipedia - Web Scraping](https://en.wikipedia.org/wiki/Web_scraping)).
2. Use your browser’s developer tools (`Inspect Element`) to:
   - Identify the title of the page.
   - Locate the first paragraph and examine its structure.
   - Explore headers (`<h1>, <h2>, <h3>`) and links (`<a>`).

### **How the DOM Is Structured:**
The DOM is a hierarchical tree structure. Here's an example:
```html
<html>
  <head>
    <title>Web Scraping</title>
  </head>
  <body>
    <h1>Introduction</h1>
    <p>This is an example paragraph.</p>
    <a href="https://example.com">Example Link</a>
  </body>
</html>
```

---

## **9.2 Web Scraping Tools: Requests and BeautifulSoup**

### **Overview**
To scrape data from a web page, two primary libraries are commonly used in Python:
- **`Requests`**: A library for sending HTTP requests and fetching web pages.
- **`BeautifulSoup`**: A library for parsing HTML and extracting elements from the parsed content.

### **Steps to Web Scraping:**
1. Send an HTTP GET request using `Requests`.
2. Parse the HTML content using `BeautifulSoup`.
3. Extract the desired elements using tags, attributes, or CSS selectors.

### **Example Code: Extracting Page Title**
```python
import requests
from bs4 import BeautifulSoup

# Fetch the web page
url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract and print the page title
title = soup.title.string
print(f"Page Title: {title}")
```

---

## **9.3 Extracting Specific Data**

### **Task: Extract All Bold Text and Images**
With `BeautifulSoup`, we can use methods like `find_all()` to locate and extract specific HTML elements.

### **Example Code: Extracting Bold Text and Images**
```python
# Extract all bold text
bold_texts = [tag.get_text() for tag in soup.find_all('b')]
print("Bold Texts:", bold_texts)

# Extract all images with their src attributes
images = [(img['src']) for img in soup.find_all('img') if 'src' in img.attrs]
print("Image Sources:", images)
```

---

## **9.4 Ethical Web Scraping**

### **Overview**
While web scraping can be a powerful tool, it is important to follow ethical guidelines and respect website owners’ wishes to avoid excessive server load and legal issues.

### **Key Concepts:**
- **What is `robots.txt`?**
  - A file that specifies which sections of a website can or cannot be accessed by web crawlers.
- **Why is `robots.txt` important?**
  - It helps website owners control the traffic to their site and avoid server overload.
  - Ethical scraping involves reviewing and adhering to the rules set in `robots.txt`.

### **Activity: Explore `robots.txt` for Wikipedia**
1. Access the `robots.txt` file for Wikipedia: [Wikipedia Robots.txt](https://en.wikipedia.org/robots.txt).
2. Identify restricted sections of the site.
3. Discuss why these sections are restricted.

### **Example Code: Accessing `robots.txt`**
```python
robots_url = "https://en.wikipedia.org/robots.txt"
robots_response = requests.get(robots_url)
print(robots_response.text)
```

---

## **9.5 Scraping Additional Data**

### **Overview**
After scraping basic data, you can refine your scraping strategy to focus on specific sections of a webpage.

### **Example Task: Scrape the "See also" Section**
```python
# Find the "See also" section
see_also_section = soup.find('span', id="See_also")
if see_also_section:
    see_also_list = see_also_section.find_next('ul')
    links = [a.get_text() for a in see_also_list.find_all('a')]
    print("See Also Links:", links)
else:
    print("No 'See also' section found.")
```

### **Testing on Another Page:**
Test the script on different Wikipedia pages to ensure consistency and robustness.

---

## **9.6 Managing Requests and Handling Errors**

### **Overview**
When scraping large numbers of web pages, managing requests responsibly is essential. Techniques include delaying requests, retrying failed requests, and handling connection errors.

### **Key Techniques:**
1. **Delaying Requests**: Introduce time delays between requests to avoid overloading the server.
   ```python
   import time
   time.sleep(2)  # Delay for 2 seconds
   ```
2. **Retrying Requests**: Use retry logic for handling failed requests.
   ```python
   import requests
   from time import sleep

   def fetch_page(url, retries=3):
       for i in range(retries):
           try:
               response = requests.get(url)
               if response.status_code == 200:
                   return response
           except requests.RequestException as e:
               print(f"Error fetching {url}: {e}")
               sleep(2)  # Wait before retrying
       return None
   ```

### **Handling Errors:**
Use `try-except` blocks to handle potential errors, such as timeouts or missing elements.
```python
try:
    element = soup.find('div', class_='nonexistent')
    print(element.get_text())
except AttributeError:
    print("Element not found!")
```

---

## **9.7 Saving Scraped Data**

### **Overview**
Once you've scraped valuable data, you may want to save it in a structured format, such as CSV or JSON.

### **Saving Data to CSV:**
```python
import csv

# Save extracted data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Link"])
    for link in links:
        writer.writerow([link])
```

### **Saving Data to JSON:**
```python
import json

# Save data to a JSON file
data = {"links": links}
with open('scraped_data.json', 'w') as json_file:
    json.dump(data, json_file)
```

---

## **Summary**

In this lesson, you learned:
1. How to understand the structure of web pages using HTML and the DOM.
2. How to use Python libraries `Requests` and `BeautifulSoup` for web scraping.
3. Ethical considerations of web scraping, including respecting `robots.txt`.
4. Techniques for extracting specific data, handling errors, and managing requests.
5. How to save scraped data to CSV and JSON formats for future use.

### **Important Notes:**
- Always respect the website’s `robots.txt` file and terms of service.
- Avoid overloading a server with excessive scraping requests.
- Use appropriate delay and retry mechanisms to manage web traffic.

For further learning, explore the [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and the [Requests Library Documentation](https://docs.python-requests.org/).

