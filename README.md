# eventel_docker_error
Demonstration of bug in eventlet. Reproduced only on ubuntu 18.04

# Steps to reproduce

    docker-compose up -d



    docker-compose exec test bash
    pip install eventlet redis
    python test/test.py


You'll get before redis. Deadlock apears.
Problem not in redis. You can check that by

    python test/test_ok.py


# Outputs

test.py

    # python test/test.py
    before redis

test_ok.py

    # python test/test_ok.py
    before redis
    after redis
