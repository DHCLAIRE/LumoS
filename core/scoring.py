#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

def evaluate_response(response_text: str):
    # Later: use NLP or rule-based evaluation
    # For now: random mock score
    return {
            "memory": random.randint(0, 5),
        "attention": random.randint(0, 5),
        "language": random.randint(0, 5)
    }
