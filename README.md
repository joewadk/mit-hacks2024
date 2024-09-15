## Installation
To install all of the frontend dependencies, go inside the `app` directory and run:
```bash
npm install
```
To install all of the backend dependencies, you'll need to first make a virtual environment like so :
```bash
py -m venv .venv
```
Next, you'll want to activate the venv like so:
```bash
.venv/Scripts/activate
```
Now navigate to the `backend` directory.
Then, you'll want to install all backend dependencies:
```bash
pip install -r requirements.txt
```

Also, please note that this is an AI agent using OpenAI, and so you'll need a `.env` file containing your api key inside the root directory. The structure is 

```bash
OPENAI_API_KEY = sk-proj......
```

## Getting Started

First, run the frontend inside the app directory:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```
Then, run the development server inside the backend directory:
```bash
py app.py
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the frontend.
