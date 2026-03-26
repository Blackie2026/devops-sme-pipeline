# Version 2 - Performance test run
from flask import Flask, jsonify
import pandas as pd
import os
from app.main import app

application = app

if __name__ == '__main__':
    application.run()
