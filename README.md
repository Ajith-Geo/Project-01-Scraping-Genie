# Project-01-Scraping-Genie
A Web scraping tool for E-Commerce websites

DEPENDANCIES to be installed:
1) python
2) pip install requests
3) pip install bs4
4) pip install lxml

This web scraping project designed to extract information about products from different e-commerce websites, namely Amazon, Flipkart, and Reliance Digital. The script takes a product category and user input as input and returns a dictionary containing product information such as title, price, and image URL.

The code utilizes the following libraries:

BeautifulSoup: A Python library for parsing HTML and XML documents. requests: A library for making HTTP requests to fetch web pages. json: For reading JSON data. concurrent.futures: For parallel execution of functions using multi-threading. Below is the detailed documentation for the provided web scraping code:

Function: main(category_from_web, user_input_from_web) This is the main function that orchestrates the web scraping process.

Parameters:

category_from_web: A string representing the category of products to search for (e.g., "laptops", "mobiles", etc.). user_input_from_web: A string representing the user input or search query for the products. Returns:

A dictionary containing the scraped product information from different e-commerce websites. Function: link_constructor(category) This function constructs search URLs for different e-commerce websites based on the given product category and user input.

Parameters:

category: A string representing the product category for which the search URLs are to be constructed. Returns:

A tuple containing a list of constructed search URLs and a list of e-commerce website names (category keys). Function: main_parser_executer() This function executes the web scraping functions for Amazon, Flipkart, and Reliance Digital in parallel using multi-threading.

Returns:

A dictionary containing the scraped product information from different e-commerce websites. Function: amazon_parser(constructed_links, category_keys, input_from_web) This function handles the web scraping for Amazon website.

Parameters:

constructed_links: A list of constructed search URLs for Amazon. category_keys: A list of e-commerce website names (category keys). input_from_web: The user input or search query for the products. Returns:

A dictionary containing the scraped product information from Amazon if found, otherwise "No results found on Amazon". Function: flipkart_parser(constructed_links, category_keys) This function handles the web scraping for Flipkart website.

Parameters:

constructed_links: A list of constructed search URLs for Flipkart. category_keys: A list of e-commerce website names (category keys). Returns:

A dictionary containing the scraped product information from Flipkart if found, otherwise "No results found on Flipkart". Function: reliance_parser(constructed_links, category_keys) This function handles the web scraping for Reliance Digital website.

Parameters:

constructed_links: A list of constructed search URLs for Reliance Digital. category_keys: A list of e-commerce website names (category keys). Returns:

A dictionary containing the scraped product information from Reliance Digital if found, otherwise "No results found on Reliance Digital". Function: generator() This function generates a random User-Agent string that is used in the HTTP headers of the requests to the websites. It helps in preventing blocking from websites due to excessive requests.

Returns:

A random User-Agent string. Important Notes: The script uses BeautifulSoup for parsing the HTML content of the websites, and it assumes that the structure of the websites may change over time. Therefore, the code may need adjustments if the structure of the websites is updated.

The script loads product information from a JSON file named "hello.json" containing the website URLs and their respective search URL patterns. This file should be present in the specified path (C:/Users/masge/Downloads/hello.json). Make sure to have this JSON file with the correct website information for the code to work correctly. The script uses multi-threading to improve the efficiency of web scraping. However, keep in mind that aggressive scraping can lead to IP blocking or temporary bans from the websites. Always respect the website's terms of service and robots.txt guidelines while web scraping.

The code contains comments that provide information about different parts of the script and explain its functionality.

Notable Points and Considerations: The code assumes that the product information is present in specific HTML elements and classes for each e-commerce website. Any changes in the website structure may require updating the code to locate the relevant elements correctly.

The script currently searches for products based on the user's input by splitting the input into individual words and searching for products containing all the input words in their title. This can be customized or extended to implement more sophisticated search criteria.

The function generator() randomly selects a User-Agent string from a predefined list of user agents. The use of different User-Agent strings helps to prevent websites from detecting and blocking web scraping activities. However, the list of user agents may become outdated over time, and it is recommended to update the list with recent user agents periodically.

The code is designed to handle different variations of product listings on each website. It checks for different HTML classes to identify the correct containers holding the product information. This helps in accommodating changes in the website layout without breaking the scraping process.

The script handles different cases of product listings on Flipkart based on the presence of specific HTML classes (common_1, common_2, common_3) in the container. These cases are specific to the website structure at the time of development.

The code uses multi-threading (ThreadPoolExecutor) to execute web scraping functions in parallel. This approach can significantly improve the overall performance by fetching data from multiple websites simultaneously. However, depending on the system's capabilities, it might be better to control the number of concurrent threads to avoid excessive resource usage.

The header variable contains the User-Agent string that will be included in the HTTP request headers. This can be useful for mimicking requests from different browsers or devices.

The code currently saves the scraped data in a dictionary with the website names ("Amazon", "Flipkart", "Reliance") as keys. If a website does not return any results, the respective key is not included in the final result dictionary.

The code does not handle exceptions and errors in depth. For robust production usage, it is essential to implement proper error handling to handle connection errors, parsing errors, or any unexpected responses from the websites.

The code is functional but may require additional enhancements, validation checks, and error handling to make it production-ready and suitable for real-world use cases.

Conclusion: The web scraping project above demonstrates a basic implementation of scraping product information from three e-commerce websites (Amazon, Flipkart, Reliance Digital) based on user input. It utilizes Python's BeautifulSoup library and requests to fetch and parse HTML content from the websites.

It's important to note that web scraping may have legal and ethical implications. Before using web scraping for any purpose, make sure to review the terms of service of the target websites, comply with their rules, and be respectful of their resources and data. Additionally, ensure that the web scraping activity does not violate any laws or policies related to data privacy and usage. Always seek permission from website owners if necessary
