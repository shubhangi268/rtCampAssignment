## SauceDemo Python Playwright with BDD Framework using Behave

Automated end-to-end test suite for https://www.saucedemo.com using python playwright. 
This project includes UI tests for sorting, checkout process, and Visual test

---

### Features Covered

- Login functionality
- Product sorting:  
  - Product Names Z–A  
  - Price: High to Low  
- Checkout functionality
  - checkout flow (add to cart → checkout → confirmation)
- Visual tests
  - Capturing Screenshot of inventory page 

---
### Prerequisites

- python3
- playwright
- For BDD framework in playwright install behave package ( pip install Playwright Behave)

### Running Tests
-  To run all the scenarios together using
   - behavex Demo/Features
-  To run individual scenario using
   - behavex Demo\Features --tags=@SCREENSHOT 
