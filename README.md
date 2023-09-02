# Fetch - Rewards

This project was build in order to solve a challenge code.

## Challenge

[Challenge](https://github.com/fetch-rewards/receipt-processor-challenge/tree/main)

## Version

The challenge will be solved using python and Django in order to solve the excersise ASAP. Like GO is the target languaje of the position, it will be solved using GO, in other branch.

## Execution

In order to run each solution, Docker will be used. More especific instructions in every branch.

please use:

    git checkout python

and,

    git checkout go

to switch between branches.

To run it:

    docker-compose up

After that, you are able to consume:

    POST    http://127.0.0.1:8000/api/receipts/process/
    GET     http://127.0.0.1:8000/api/receipts/{id}/points/

Documentation are able [here](https://documenter.getpostman.com/view/843341/2s9Y5ctg6s).
