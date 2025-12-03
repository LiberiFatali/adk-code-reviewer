from setuptools import setup, find_packages

setup(
    name="code-review-assistant",
    version="1.0.0",
    description="A code review assistant powered by Google ADK and Gemini models",
    author="LiberiFatali",
    packages=find_packages(),
    install_requires=[
        "google-cloud-aiplatform[adk]>=1.111",
        "google-adk>=1.14.1",
        "pycodestyle>=2.11.0",
        "python-dotenv>=1.0.0",
        "pydantic-settings>=2.0.0",
        "structlog>=24.0.0",
        "psycopg2-binary>=2.9.0",
    ],
    python_requires=">=3.10",
)
