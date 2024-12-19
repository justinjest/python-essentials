
# **Lesson 09 — Introduction to Web Scraping**

## **Lesson Overview**
**Learning objective:** Students will learn the fundamentals of web scraping, including understanding HTML and DOM structures, using Python libraries like `BeautifulSoup` and `Requests`, and exploring the ethical considerations of web scraping.

### **Topics:**
1. Basics of HTML and DOM
2. Web Scraping Tools: `Requests` and `BeautifulSoup`
3. Ethical Web Scraping: Understanding `robots.txt` and ethical considerations

---

## **9.1 Basics of HTML and DOM**

### **Overview**
HTML (Hypertext Markup Language) structures web pages, while the DOM (Document Object Model) represents the structure of a web page as a tree of elements. Understanding these concepts is critical for locating and extracting data.

### **Key HTML Elements:**
- `<title>`: The title of the page.
- `<p>`: Paragraphs of text.
- `<h1>, <h2>, <h3>`: Headers.
- `<a>`: Links with `href` attributes.
- `<img>`: Images with `src` attributes.

### **Hands-On Activity:**
1. Open the Wikipedia page for "Web Scraping" ([Wikipedia - Web Scraping](https://en.wikipedia.org/wiki/Web_scraping)).
2. Use your browser’s developer tools (`Inspect Element`) to:
   - Identify the title of the page.
   - Locate the first paragraph and note its structure.
   - Explore the headers (`<h1>, <h2>, <h3>`) and links (`<a>`).

### **How DOM Is Structured:**
The DOM is a tree-like structure with nested elements. For instance:
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
- `Requests`: A Python library for sending HTTP requests to fetch web pages.
- `BeautifulSoup`: A library for parsing HTML and extracting specific elements.

### **Steps:**
1. Send an HTTP GET request using `Requests`.
2. Parse the HTML using `BeautifulSoup`.
3. Locate elements using tags, attributes, or CSS selectors.

### **Example Code: Extracting Page Title**
```python
import requests
from bs4 import BeautifulSoup

# Fetch the web page
url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.content, "html.parser")

# Extract the title
title = soup.title.string
print(f"Page Title: {title}")
```

---

## **9.3 Extracting Specific Data**

### **Task: Extract All Bold Text and Images**
Use BeautifulSoup methods like `find_all()` to locate specific tags.

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
Web scraping must adhere to ethical and legal guidelines, including respecting `robots.txt` files and avoiding excessive server load.

### **Key Concepts:**
- **What is `robots.txt`?**
  A file that specifies which parts of a website can or cannot be accessed by crawlers.
- **Why is it important?**
  It helps website owners control web traffic and prevent server overload.

### **Activity: Explore `robots.txt` for Wikipedia**
1. Access the file: [Wikipedia Robots.txt](https://en.wikipedia.org/robots.txt).
2. Identify restricted sections of the site.
3. Reflect on why these restrictions exist.

### **Example Code: Accessing `robots.txt`**
```python
robots_url = "https://en.wikipedia.org/robots.txt"
robots_response = requests.get(robots_url)
print(robots_response.text)
```

---

## **9.5 Scraping Additional Data**

### **Overview**
Leverage BeautifulSoup to extract data from specific sections of a web page.

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
Test the script on another Wikipedia page to see consistent results.

---

## **Summary**

In this lesson, you learned:
1. How to analyze the structure of web pages using HTML and the DOM.
2. How to use Python libraries `Requests` and `BeautifulSoup` for web scraping.
3. The ethical considerations of web scraping, including adhering to `robots.txt`.
4. Techniques for extracting and parsing specific web page elements.

### **Important Notes:**
- Always respect a website’s terms of service and `robots.txt`.
- Avoid sending too many requests in a short time frame.

For further learning, explore the [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and the [Requests Library Documentation](https://docs.python-requests.org/).
