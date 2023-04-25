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

3. install flask-cors

   ```bash
   $ pip install Flask flask-cors openai
   ```
4. install python-dotenv

   ```bash
   $ pip install python-dotenv
   ```
   
5. run the app

   ```bash
   $ flask run
   ```