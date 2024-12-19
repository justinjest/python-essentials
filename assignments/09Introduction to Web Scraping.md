# **Introduction to Web Scraping**

---

## **Overview**
This lesson introduces web scraping concepts and practices, including:
1. Understanding HTML and the DOM structure.
2. Extracting content using BeautifulSoup.
3. Ethical considerations in web scraping.
4. Writing scripts to scrape specific data from web pages.

---

## **Tasks**

### **Task 1: Understanding HTML and the DOM**

**Goal**:  
Learn how web pages are structured and identify elements in the DOM.

1. Open the Wikipedia page for "Web scraping" in your browser: [Wikipedia - Web Scraping](https://en.wikipedia.org/wiki/Web_scraping).
2. Use the browser's developer tools (Inspect Element) to examine:
   - The **title** of the page.
   - The structure of the **first paragraph**.
   - The structure of the **headers** (`<h1>`, `<h2>`, `<h3>`) and **links**.
3. Write a brief description of how the DOM is structured on this page, focusing on:
   - Parent-child relationships.
   - Use of tags and attributes (like `class` or `id`).

---

### **Task 2: Extracting Elements with BeautifulSoup**

**Goal**:  
Practice extracting specific elements from a web page.

1. Using BeautifulSoup, write a script to extract:
   - All **bold text** (`<b>` tags) on the page.
   - All **images** (`<img>` tags) and their `src` attributes.
2. Run your script and document:
   - The list of bold text.
   - The list of images and their corresponding `src` attributes.

---

### **Task 3: Ethical Web Scraping**

**Goal**:  
Understand the importance of ethical web scraping and `robots.txt` files.

1. Access the `robots.txt` file for Wikipedia: [Wikipedia Robots.txt](https://en.wikipedia.org/robots.txt).
2. Analyze the file and answer the following questions using Print statements:
   - Which sections of the website are restricted for crawling?
   - Are there specific rules for certain user agents?
3. Reflect on why websites use `robots.txt` and write 2–3 sentences explaining its purpose and how it promotes ethical scraping.Use Print statements to display your reflection.

---

### **Task 4: Scraping Structured Data**

**Goal**:  
Extract and analyze data from specific sections of a web page of your choice.

1. Write a script to extract the contents of the **"See also"** section (if present) on a Wikipedia page.
   - **Hint**: Use appropriate methods to locate the section and extract its list items.
2. Test your script on another Wikipedia page of your choice.
3. Document the output, including:
   - The content extracted from the "See also" section.
   - Any challenges faced and how you resolved them.

---



**Submission**
1. Submit your completed Python code, including all tasks, in a .py file or a Jupyter notebook. Make sure to include comments explaining your code where necessary.

## **Resources**

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Python Requests Library](https://docs.python-requests.org/en/latest/)
- [MDN Web Docs: Understanding the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- [Wikipedia Robots.txt](https://en.wikipedia.org/robots.txt)

---  
