# NewsChecker_chat
## Setup
1. create .env file and add your api key to the newly created `.env` file.
```
FLASK_APP=app
FLASK_ENV=development

# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
OPENAI_API_KEY=


```

2. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

3. run the following code

   ```bash
   $ pip install Flask flask-cors openai
   ```
4. Run the app:

   ```bash
   $ pip install python-dotenv
   ```