# Alfies Checker

This is a Docker project that periodically checks the availability of products on the Austrian grocery delivery platform Alfies and sends notifications using the Pushover API.

Alfies' own implementation is slow, needs to be activated manually each time it's newly out of stock and certain product's (such as it's food waste rescue bags) cannot be properly monitored.

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/clairekardas/alfies-checker.git
    ```

2. Replace `your_user_key` and `your_api_token` in `docker-compose.yml` with your actual Pushover user key and API token respectively. You will need to create an application on Pushover to get an API token.
3. To query using your own Alfies account, it is necessary to replace `your_auth_token` with your actual Alfies authentication token. You can view it using the network capture of your browser's developer console. 

4. Build and run the Docker container:

    ```bash
    docker-compose up --build
    ```

## Configuration

You can modify the list of products to check and the intervals in `main.py`. The environment variables for Pushover API credentials are set in the `docker-compose.yml` file.

